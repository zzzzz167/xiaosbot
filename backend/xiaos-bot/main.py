import asyncio
import sys
import os
from graia.broadcast import Broadcast
from avilla import Avilla
from avilla.onebot.protocol import OnebotProtocol
from avilla.onebot.config import OnebotConfig, WebsocketCommunication
from avilla.network.clients.aiohttp import AiohttpWebsocketClient
import aiohttp
from loguru import logger
from yarl import URL
from avilla.event.message import MessageEvent
from graia.saya import Saya
from graia.saya.builtins.broadcast import BroadcastBehaviour
import api
import uvicorn

logger.remove()
logger.add(sys.stderr, level="INFO")
logger.add("bot.log", level="INFO")
logger.add("./cache/debuglogs")


loop = asyncio.get_event_loop()
bcc = Broadcast(loop=loop)
session = aiohttp.ClientSession(loop=loop)
saya = Saya(bcc)
saya.install_behaviours(BroadcastBehaviour(bcc))

app = Avilla(
    bcc,
    OnebotProtocol,
    {"ws": AiohttpWebsocketClient(session)},
    {
        OnebotProtocol: OnebotConfig(
            access_token="",
            bot_id=2167784388,
            communications={
                "ws": WebsocketCommunication(
                    api_root=URL("ws://127.0.0.1:6700")
                    )
            },
        )
    },
    logger=logger
)

ignore = ["__pycache__"]
with saya.module_context():
    for module in os.listdir("modules"):
        if module in ignore:
            continue
        try:
            if os.path.isdir(module):
                saya.require(f"modules.{module}")
            else:
                saya.require(f"modules.{module.split('.')[0]}")
        except ModuleNotFoundError:
            pass

api_launched = False


@bcc.receiver(MessageEvent)
async def on_launch():
    global api_launched
    if api_launched:
        return
    api_launched = True
    app.logger.info("Try to launch api")
    api.saya = saya
    api.avilla = app
    await asyncio.to_thread(uvicorn.run,
                            app=api.app,
                            host="0.0.0.0",
                            port=6010)

if __name__ == "__main__":
    try:
        loop.run_until_complete(app.launch())
        loop.run_forever()
    except KeyboardInterrupt:
        logger.info("bye~ have a nice day!")
        quit()

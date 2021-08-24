from graia.saya import Saya, Channel
from graia.saya.builtins.broadcast.schema import ListenerSchema
from avilla.event.message import MessageEvent
from avilla.execution.message import MessageSend
from avilla.message.chain import MessageChain
from avilla.builtins.elements import PlainText
from avilla.relationship import Relationship
saya = Saya.current()
channel = Channel.current()


@channel.use(ListenerSchema(
    listening_events=[MessageEvent]  # 填入你需要监听的事件
))
async def module_listener(event: MessageEvent, rs: Relationship):
    if event.message.as_display() == "/test":
        await rs.exec(
            MessageSend(MessageChain.create([PlainText("test infomation")]))
        )

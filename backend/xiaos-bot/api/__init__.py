import os
import datetime
import platform
import psutil
import socket
import asyncio
from fastapi import FastAPI, WebSocketDisconnect, WebSocket
from graia.saya import Saya
from avilla import Avilla
from fastapi.middleware.cors import CORSMiddleware

start_time = datetime.datetime.now()
saya: Saya
avilla: Avilla
avilla_v = os.popen("pip show avilla-core").readlines()[1].split(" ")[1]

memory = psutil.virtual_memory()
total_nc = round((float(memory.total) / 1024 / 1024 / 1024), 2)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip


def get_sys_status_sync():
    v_mem = psutil.virtual_memory()
    s_mem = psutil.swap_memory()
    cpu_percent = str(psutil.cpu_percent(0))
    cpu_tem = str(psutil.sensors_temperatures()["cpu_thermal"][0].current)
    v_mem_percent = str(v_mem.percent)
    s_mem_percent = str(s_mem.percent)
    return {"cpuUse": cpu_percent,
            "cpuTem": cpu_tem,
            "vMemUse": v_mem_percent,
            "sMemUse": s_mem_percent}


@app.get("/")
async def root():
    return {"message": "Hello, World!"}


@app.get("/sys-info")
async def sysInfo():
    return {"cpuInfo": str(platform.machine()),
            "cpuCores": str(psutil.cpu_count()),
            "sysInfo": str(platform.platform())+str(platform.version()),
            "platform": str(platform.system()),
            "pythonVersion": str(platform.python_revision()),
            "startTime": str(start_time),
            "ipHost": str(get_host_ip()),
            "memorySize": str(total_nc),
            "sayaVersion": str(avilla_v)}


@app.websocket("/ws/sys-status")
async def get_sys_status(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            resp = await asyncio.to_thread(get_sys_status_sync)
            await ws.send_json(resp)
            await asyncio.sleep(2)
    except WebSocketDisconnect:
        await ws.close()

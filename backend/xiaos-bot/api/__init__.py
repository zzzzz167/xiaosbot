import os
import datetime
from fastapi import FastAPI
from graia.saya import Saya
from avilla import Avilla
from fastapi.middleware.cors import CORSMiddleware
import platform
import psutil
import socket

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

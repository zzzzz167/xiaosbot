import datetime
from fastapi import FastAPI
from graia.saya import Saya
from avilla import Avilla

start_time = datetime.datetime.now()
saya: Saya
avilla: Avilla

app = FastAPI(
    allow_origin_regex=".*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}

from fastapi import FastAPI, Response, status
from fastapi import Request

import docker
import sdk
from utils.header import meta_extract

app = FastAPI()
client = docker.from_env()

sdk.use_docker()


@app.get("/ping", status_code=200)
async def root():
    return "pong"


@app.get("/{path:path}")
async def proxy_get(path: str, req: Request):
    app_name, app_port = meta_extract(req)
    try:
        app = client.containers.get(app_name)
    except:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return app.get(app_port, path)


@app.post("/{path:path}")
async def proxy_get(path: str, req: Request):
    app_name, app_port = meta_extract(req)
    body = await req.json()
    app_name = 'vigorous_sinoussi'
    app_port = 80
    try:
        app = client.containers.get(app_name)
    except:
        return Response(status_code=status.HTTP_400_BAD_REQUEST)
    return app.post(app_port, path, body)

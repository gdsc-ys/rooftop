from fastapi import FastAPI
from fastapi import Request
import docker
import sdk


app = FastAPI()
client = docker.from_env()

sdk.use_docker()

@app.get("/ping", status_code=200)
async def root():
    return "alive"


@app.get("/{path_params:path}")
async def proxy_get(path_params: str, req: Request):
    host = req.headers['host']
    app_name = host.split(':')[0].split('.')[0]
    port = host.split(':')[-1]

    return {
        'app': app_name,
        'port': port,
        'path': path_params
    }

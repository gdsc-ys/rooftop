from fastapi import Request


def meta_extract(req: Request):
    host = req.headers['host']
    container_name = host.split(':')[0].split('.')[0]
    container_port = host.split(':')[-1]
    return container_name, container_port

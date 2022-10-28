import docker
import sdk


sdk.use_docker()

client = docker.from_env()

print(client.containers.list())
cont = client.containers.get('vigorous_sinoussi')
_, output = cont.exec_run('curl localhost:80')
# print(output.decode('utf-8'))

print(cont.exec_run_t())

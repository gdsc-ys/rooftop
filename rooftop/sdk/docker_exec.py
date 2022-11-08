import subprocess
from docker.models.containers import Container


def _docker_exec_run_get(self, port, path):
    ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    return ret.stdout


def _docker_exec_run_post(self, port, path, data):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', '-f', '-H', 'Content-Type: application/json', '-d', f'"{data}"', '-X', 'POST', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_put(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_delete(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_options(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_head(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_patch(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def _docker_exec_run_trace(self, port, path):
    pass
    # ret = subprocess.run(['docker', 'exec', '-t', self.name, 'curl', f'localhost:{port}/{path}'], encoding='utf-8', capture_output=True)
    # return ret.stdout


def use_docker():
    Container.get = _docker_exec_run_get
    Container.post = _docker_exec_run_post
    Container.put = _docker_exec_run_put
    Container.delete = _docker_exec_run_delete
    Container.options = _docker_exec_run_options
    Container.head = _docker_exec_run_head
    Container.patch = _docker_exec_run_patch
    Container.trace = _docker_exec_run_trace

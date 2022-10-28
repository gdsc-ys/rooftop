import subprocess
from docker.models.containers import Container


def _docker_exec_run_t(self):
    return subprocess.call(['docker', 'exec', '-t', self.name, 'curl', 'localhost'])


def use_docker():
    Container.exec_run_t = _docker_exec_run_t

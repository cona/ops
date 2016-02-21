#coding:utf-8
from fabric.api import run sudo

def docker():
    sudo('yum update')
    run('curl -fsSL https://get.docker.com/ | sh')
    sudo('service docker start')
    sudo('usermod -aG docker `whoami`')
    sudo('chkconfig docker on')


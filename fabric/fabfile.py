#coding:utf-8
from fabric.api import run,sudo

def docker():
    sudo('yum -y update')
    run('curl -fsSL https://get.docker.com/ | sh')
    sudo('service docker start')
    sudo('usermod -aG docker `whoami`')
    sudo('chkconfig docker on')
    run('docker -v')
def nginx():
    sudo('yum -y install http://nginx.org/packages/centos/7/noarch/RPMS/nginx-release-centos-7-0.el7.ngx.noarch.rpm')
    sudo('yum -y install --enablerepo=nginx nginx')
    sudo('systemctl enable nginx')
    sudo('systemctl start nginx')
    sudo('firewall-cmd --permanent --zone=public --add-service=http')
    sudo('firewall-cmd --reload')
def composer():
    sudo('yum -y install php')
    run('curl -sS https://getcomposer.org/installer | php')
    run('php composer.phar')

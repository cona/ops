#!/bin/sh
yum clean all && yum -y update && yum makecache
yum -y install  python-setuptools gcc python-devel
easy_install pip
pip install pycrypto fabric
fab -V


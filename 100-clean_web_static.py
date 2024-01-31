#!/usr/bin/python3
""" Function that cleans by deleting out-of-date archives"""
from fabric.api import *


env.hosts = ['18.207.1.233', '52.91.135.48']
env.user = "ubuntu"


def do_clean(number=0):
    """ CLEANS FUNCTION """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))

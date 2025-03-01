#!/usr/bin/python3
""" Function that compress a folder """
from datetime import datetime
from fabric.api import *
import shlex
import os


env.hosts = ['54.242.111.189', '54.175.159.23']
env.user = "ubuntu"


def deploy():
    """ Launch the deployment """
    try:
        archive_path = do_pack()
    except Exception:
        return False

    return do_deploy(archive_path)


def do_pack():
    """ Pack Folder """
    try:
        if not os.path.exists("versions"):
            local('mkdir versions')
        CurrentDateTime = datetime.now().strftime("%Y%m%d%H%M%S")
        ArchivePath = 'versions/web_static_{}.tgz'.format(CurrentDateTime)
        local('tar -cvzf {} web_static'.format(ArchivePath))
        return ArchivePath
    except Exception:
        return None


def do_deploy(archive_path):
    """ Deploys """
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]
        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)
        put(archive_path, "/tmp/")

        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))

        print("New version deployed!")

        return True
    except Exception:
        return False

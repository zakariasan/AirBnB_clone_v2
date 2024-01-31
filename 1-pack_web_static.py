#!/usr/bin/python3
""" compress a folder and name it the  current time and date """
from datetime import datetime
from fabric.api import local
import os


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

#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

env.hosts = ['104.196.57.225', '35.231.8.144']
env.user = 'ubuntu'


def do_pack():
    """
    generates a .tgz archive from the contents of the web_static folder
    of AirBnB Clone repo
    """
    try:
        date = datetime.now()
        file_name = "web_static_{}{}{}{}{}{}.tgz".\
                    format(date.year, date.month, date.day,
                           date.hour, date.minute, date.second)
        local("mkdir -p versions")
        local("tar -cvzf versions/{} web_static".format(file_name))
        print("web_static packed: versions/{} -> {}".
              format(file_name, os.path.getsize(file_name)))
    except:
        return None


def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """
    if os.path.exists(archive_path) is False:
        return False

    arch_filename_ext = archive_path.split("/")[1]
    arch_filename_w_ext = archive_path.split(".")[0]
    unc_archive = "/data/web_static/releases/{}/".format(arch_filename_w_ext)
    try:
        put(archive_path, "/tmp")
        run("mkdir -p {}".format(unc_archive))
        run("tar -xzf /tmp/{} -C {}".format(arch_filename_ext, unc_archive))
        run("rm /tmp/{}".format(arch_filename_ext))
        run("mv {}/web_static/* {}".format(unc_archive, unc_archive))
        run("rm -rf {}/web_static".format(unc_archive))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(unc_archive))
        return True
    except:
        return False


def deploy():
    """
    creates and distributes an archive to your web servers,
    using the function deploy
    """
    try:
        do_pack()
        result = do_deploy(archive_path)
        return result
    except:
        return False

#!/usr/bin/python3
"""
    Deploys the archive to web server
"""

from fabric.api import *
from datetime import datetime
import os
env.hosts = ['35.237.197.183', '35.237.134.117']


def do_pack():
    """
        compresses a folder to a .tgz archive
    """
    tar_cmd = "sudo tar -cvzf "
    mkdir_cmd = "sudo mkdir -p versions/"
    date_string = datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        local(mkdir_cmd)
        local(tar_cmd + "versions/web_static_{}.tgz "
              .format(date_string) + "web_static")
        return "versions/web_static_{}.tgz".format(date_string)
    except BaseException:
        return None

def do_deploy(archive_path):
    """
        deploy the archive to the webservers
    """
    filename_wo_ext = archive_path[9:34]
    filename_w_ext = archive_path[9:]
    input_path = "/data/web_static/releases/{}/".format(filename_wo_ext)

    if os.path.exists(archive_path) is False:
        return False
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("sudo tar -zxvf /tmp/{} -C {}".format(filename_w_ext, input_path))
        run("sudo rm -rf /tmp/{}".format(filename_w_ext))
        run("sudo mv -n {}/web_static/* {}".format(input_path, input_path))
        run("sudo rm -rf {}/web_static".format(input_path))
        run("sudo rm /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(input_path))
        return True

    except BaseException:
        return False

def deploy():
    """
        packs and deploys a web_static folder to a web server
    """
    return_pack = do_pack()
    if return_pack is None:
        return False
    return do_deploy(return_pack)

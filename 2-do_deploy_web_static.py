#!/usr/bin/python3
"""
    Deploys the archive to web server
"""

from fabric.api import *
from datetime import datetime


def do_deploy(archive_path):
    """
        deploy the archive to the webservers
    """
    env.hosts = ['35.237.197.183', '35.237.134.117']
    filename_wo_ext = archive_path[9:34]
    filename_w_ext = archive_path[9:]
    input_path = "/data/web_static/releases/{}/".format(filename_wo_ext)
    try:
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(input_path))
        run("tar -zxvf /tmp/{} -C {}".format(filename_w_ext, input_path))
        run("sudo rm /tmp/{}".format(filename_w_ext))
        run("sudo rm /data/web_static/current")
        run("sudo ln -sf /data/web_static/releases/{}/ 
            /data/web_static/current".format(filename_wo_ext))
        return True

    except:
        return False

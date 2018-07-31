#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os


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
    except:
        return False

#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os


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
        local("mkdir versions")
        local("tar -cfvz versions/{} web_static".format(file_name))
        print("web_static packed: {} -> {}".
              format(file_name, os.path.getsize(file_name)))
    except:
        return None

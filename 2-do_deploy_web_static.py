#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

def do_deploy(archive_path):
    """
    distributes an archive to web servers
    """

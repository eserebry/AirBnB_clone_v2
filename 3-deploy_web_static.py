#!/usr/bin/python3
from fabric.api import *
from datetime import datetime
import os

def deploy():
    """
    creates and distributes an archive to your web servers,
    using the function deploy
    """

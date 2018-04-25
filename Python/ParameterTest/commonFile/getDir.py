# !/usr/bin/python3

"""
FileName    : getDir.py
Author      : ken
Date        : 2018-04-21
Describe    : get path
"""
import os

currentDir = os.path.abspath(os.path.dirname(__file__))
proDir = os.path.split(currentDir)[0]

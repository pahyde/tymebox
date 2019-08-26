import click
import os
import json
from colorama import init


#OS

def read_json(file_path, type=dict):
    try:
        curr = os.getcwd()
        os.chdir(file_path)
        with open('groups.json', 'r') as fp:
            return json.load(fp)
        os.chdir(curr)
    except IOError:
        return type()


def write_json(data, dir, file_path):
    if not os.path.exists(file_path):
        os.makedirs(file_path, exist_ok=True)
    curr = os.getcwd()
    os.chdir(file_path)
    with open('groups.json', 'w') as fp:
        json.dump(data,fp)
    os.chdir(curr)



#UI

red     = lambda s: '\033[31m' + s + '\033[39m'
green   = lambda s: '\033[32m' + s + '\033[39m'
yellow  = lambda s: '\033[33m' + s + '\033[39m'
blue    = lambda s: '\033[34m' + s + '\033[39m'
magenta = lambda s: '\033[35m' + s + '\033[39m'
cyan    = lambda s: '\033[36m' + s + '\033[39m'


def progress_bar():
    pass
import os
import sys
import requests

from src.scripts.base_script import BaseScript, log_error

argv = sys.argv[1:]





def checkup():
    res = requests.get('https://github.com/xiezi222/wife_helper/tree/main/src/scripts')
    print(res.text)

class Script():
    # def __init__(self):

    def run(self):
        print("args==argv==", argv)
        log_error("asdada")
        checkup()


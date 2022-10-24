import os
import sys
from base_script import BaseScript, log_error

argv = sys.argv[1:]


class Test(BaseScript):
    # def __init__(self):

    def executive(self):
        print("args==argv==", argv)
        log_error("asdada")


Test().run()

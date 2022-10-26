#!usr/bin/python3
# -*- coding: UTF-8 -*-

import requests as http
import re
import os


class CheckUp:

    def get_init_file(self):
        url = 'https://raw.githubusercontent.com/xiezi222/wife_helper/main/src/scripts/__init__.py'
        res = http.get(url)
        return res.text

    def check(self):
        info = self.get_init_file()
        name_list = re.findall("'(.*?)'", info)
        print( name_list)
        base_path = 'https://raw.githubusercontent.com/xiezi222/wife_helper/main/src/scripts/'
        base_save_path = os.path.join(os.getcwd(), 'src', 'scripts')
        if not os.path.exists(base_save_path):
            os.makedirs(base_save_path)

        for name in name_list:
            script_url = base_path+name+".py"
            res = http.get(script_url)

            if res.status_code == 200:
                save_path = os.path.join(base_save_path, name + ".py")
                print("save_path:" + save_path)
                self.save(res.text, save_path)
    def save(self, content, path):
        filew = open(path, mode='w', encoding="utf-8")
        filew.write(content)
        filew.close()

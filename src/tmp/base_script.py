#!/usr/bin/python3
# -*- coding: UTF-8 -*-

from datetime import datetime


class BaseScript:
    def executive(self):
        pass

    def run(self):
        print("开始执行任务……")
        start_time = datetime.now()
        self.executive()
        delta = (datetime.now() - start_time).seconds
        print("任务执行完毕, 共耗时:", int(delta / 60), "分", delta % 60, "秒")



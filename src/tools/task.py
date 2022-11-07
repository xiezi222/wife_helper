import os
import sys
import time

for i in range(5):
    print("task {}\n".format(i))
    sys.stdout.flush()
    time.sleep(1)
for i in range(5):
    print("task {}\n".format(i))
    sys.stderr.flush()
    time.sleep(1)
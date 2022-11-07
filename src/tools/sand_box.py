import shlex
import subprocess


class SandBox:
    def run(self):
        shell_cmd = "python task.py"
        cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(cmd,
                             shell=False,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT)
        while p.poll() is None:
            line = p.stdout.readline()
            line = line.strip()
            if line:
                print("task output:[{}]".format(line))
        if p.returncode == 0:
            print("exit 0")
        else:
            print("error")


if __name__ == '__mian__':
    SandBox().run()
    while True:
        print("1")

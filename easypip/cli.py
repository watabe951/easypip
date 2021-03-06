import subprocess
import sys
import argparse
import os

env = dict(os.environ)
def init():
    p = subprocess.Popen(["python", "-m", "venv", ".venv"], env=env, shell=True)

    p.wait()

def lock():
    # With --all option, pip freeze command output includes wheel, pip, setuptools. 
    p = subprocess.Popen(["pip", "freeze", "--all"], encoding='utf-8', stdout=subprocess.PIPE, env=env, shell=True)

    p.wait()
    lines = p.stdout.readlines()
    print(lines)
    with open("reqirements.lock", "w") as f:
        for line in lines:
            f.write(line)
def sync():
    # run
    p = subprocess.Popen(["pip", "install", "-r", "reqirements.lock"], env=env, shell=True)

    p.wait()
def test_pip():
    # run
    po = subprocess.Popen(["which", "pip"], env=env, shell=True)

    po.wait()


def main():
    # parse
    parser = argparse.ArgumentParser(description="easypip is a thin wrapper of pip")
    parser.add_argument('arg', type=str, nargs='*', help='arguments to pass to pip command')
    args = parser.parse_args()
    if len(args.arg) == 0:
        executable = ["pip"]
        # run
        po = subprocess.Popen(executable, env=env, shell=True)

        po.wait()
        return
    if args.arg[0] == "sync":
        sync()
    elif args.arg[0] == "lock":
        lock()
    elif args.arg[0] == "install":
        executable = ["pip"] + args.arg
        # run
        po = subprocess.Popen(executable, env=env, shell=True)

        po.wait()
        # lock
        lock()
    elif args.arg[0] == "uninstall":
        executable = ["pip"] + args.arg
        # run
        po = subprocess.Popen(executable, env=env, shell=True)

        po.wait()
        # lock
        lock()
    elif args.arg[0] == "init":
        init()
    else:
        executable = ["pip"] + args.arg
        print(executable)
        # run
        po = subprocess.Popen(executable, encoding='utf-8', env=env, shell=True)

        po.wait()
if __name__ == "__main__":
    main()

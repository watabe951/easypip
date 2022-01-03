import subprocess
import sys
import argparse
def lock():
    # With --all option, pip freeze command output includes wheel, pip, setuptools. 
    p = subprocess.Popen(["pip", "freeze", "--all"], encoding='utf-8', stdout=subprocess.PIPE)

    p.wait()
    lines = p.stdout.readlines()
    print(lines)
    with open("reqirements.lock", "w") as f:
        for line in lines:
            f.write(line)
def sync(args):
    # run
    p = subprocess.Popen(["pip", "install", "-r", "reqirements.lock"])

    p.wait()

def main():
    # parse
    parser = argparse.ArgumentParser(description="easypip is a thin wrapper of pip")
    parser.add_argument('arg', type=str, nargs='*', help='arguments to pass to pip command')
    args = parser.parse_args()

    if args.arg[0] == "sync":
        sync(args)
    elif args.arg[0] == "lock":
        lock(args)
    elif args.arg[0] == "install":
        executable = ["pip"] + args.arg
        print(executable)
        # run
        po = subprocess.Popen(executable)

        po.wait()
        # lock
        lock()
    elif args.arg[0] == "uninstall":
        executable = ["pip"] + args.arg
        print(executable)
        # run
        po = subprocess.Popen(executable)

        po.wait()
        # lock
        lock()

    else:
        executable = ["pip"] + args.arg
        print(executable)
        # run
        po = subprocess.Popen(executable, encoding='utf-8', stdout=subprocess.PIPE)

        po.wait()
        lines = po.stdout.readlines()
        print(lines)
if __name__ == "__main__":
    main()

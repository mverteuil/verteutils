#!/usr/bin/env python
import os
import sys
import subprocess
import optparse
import signal

def ping(server, port):
    result = subprocess.call([
        "nc", "-w", "1",
        server, "-z", port
    ])
    return result

def main(server, port=22, ssh_args=None):
    while ping(server, port):
        pass
    sys.stdout.flush()
    args = ["/usr/bin/ssh", server, "-p %s"%port] + ssh_args
    os.execv("/usr/bin/ssh", args)

if __name__ == "__main__":
    args = sys.argv[1:]
    server = args[0]
    main(server, "22", args[1:])

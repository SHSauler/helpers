#!/usr/bin/env python3

import os
import sys

PIDFILE = "/tmp/pidcheck.pid"


def set_pidfile(pidfile=PIDFILE):
    pid = str(os.getpid())
    
    with open(pidfile, 'w') as f:
        print(pid, file=f)


def get_pid():
    if os.path.isfile(PIDFILE):
        with open(PIDFILE) as pidfile:
            pid = pidfile.readline()
        return int(pid)
    return False


def check_pid(pid):
    """ Check For the existence of a unix pid. """
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def unset_pidfile(pidfile=PIDFILE):
    os.unlink(pidfile)


set_pidfile()
pid_num = get_pid()
print("PID is {0}".format(pid_num))
print(check_pid(pid_num))
unset_pidfile()

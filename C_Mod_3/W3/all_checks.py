#!/usr/bin/env python 

import shutil 
import sys
import os 

def check_reboot():
    """Returns True if the computer has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def check_dick_full(disk, min_gb, min_percent):
    """Returns True if there is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total 
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True 
    return False

def main():

    if check_reboot():
        print("Pending Reboot")
        sys.exit(1)
    if check_reboot("/", 2, 10):
        print("ERROR: not enough disk space")
        sys.exit(1)
    print("Everything ok")
    sys.exit(0)

main()
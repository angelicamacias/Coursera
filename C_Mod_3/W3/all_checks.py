import shutil 
import sys

def check_dick_usage(disk, min_absolut, min_percent):
    """Returns True if there is enough free disk space, false otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total 
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_absolut:
        return True 
    return False

def main():

    if not check_dick_usage("/", 2, 10):
        print("ERROR: not enough disk space")
        sys.exit(1)

    print("Everything ok")
    sys.exit(0)
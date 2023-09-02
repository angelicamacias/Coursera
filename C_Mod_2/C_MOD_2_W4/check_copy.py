#!/usr/bin/env python 

import re 
import sys

logfile = sys.argv[1]
with open(logfile) as f: 
    for line in f: 
        if "CRON" not in line:
            continue
        print(line.strip())

############################# INTERPRETER PYTHON 
## import re
## pattern = r"USER \((\w+)\)$"
## line = "Jul 6 14:04:01 computer.name CRON[29440]: USER(naughty_user)"
## result = re.search(pattern, line)
## pirnt(result[1])
# naughty_user


$ cat changeJane.py
#!/usr/bin/env python3
import sys
import subprocess
f= open (sys.argv[1],"r")
path='/home/student-03-210cd7eda6b3'
for line in f.readlines():
 old_name = line.strip()
 new_name = old_name.replace("jane","jdoe")
 subprocess.run(["mv",path+old_name,path+new_name])
f.close()

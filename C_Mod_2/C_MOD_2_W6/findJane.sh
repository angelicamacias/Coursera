/scripts$ cat findJane.sh
#!/bin/bash

> oldFiles.txt

files=$(grep " jane " /home/student-03-210cd7eda6b3/data/list.txt | cut -d ' ' -f 3)

for i in $files;do

if test -e ~/$i;then

echo $i>>oldFiles.txt;

else echo "not working"; fi

don
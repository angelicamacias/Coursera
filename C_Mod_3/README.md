# WEEK 1

### Version Control 

- It's importat to have access to the version and history of the code beacuse: 
	- if change our code, and the new one have bug or dosen;t work in all the computer, we can go back 
	to the first version code and debug what is happend in the new one. 

- we will learn about how to use git with the command line
- we will learn about how to install git 
- The new chack verifies that the firmware of the computer, also known as the UEFI
- Git help to manatin a healthy codebase for all kinds of IT resources. 
- At the same time help to multiple people collaborate ton the same code toghter

### Keeping historical copies

- keeping historyc copies, is the wrong way becasuse this make a lot of trobles like: 
	- dont remember the name the copie
	- Have to do a copi when you do a small change 
	- save a lot of documents with the copies
	- dont have the same that you patternes

### Diffing files

- the command "diff" help us to show us the change between two files
- the syntax is: diff <file1> <file2>
- When we use the command diff we will see the symbols > < 
	< rest content 
	> add content 
- also we can use the flag -u ---> "diff -u  <file1> <file2>" this is to get more information about the changes 
	+ add lines
	- remove lines
- When we use the command diff we will see the notations: 
	- 6c6: lines 6 Change(c) 
	- 6a6: lines 6 add(a)
- Also exist more command like wdiff, these command show the words that change in place that line by line
- At the same way we can use tool online that show the changes with colors 

### Applaying changes

- with the command patch we can applay the change to the code 
	syntax: patch code.py < app_change.diff
- for applay the change we have to save the change in a file withe the exatansion "diff" for convension 
		diff app1.py app2.py > app_change.diff 
- when we have the file with the output of the change we use the command patch to put the change in the code
	patch code.py < app_change.diff
- if the result is success then we will have just one line the output: "patchin files <namefile>"
- but what do this in place to copy the new code in another fies? the principal reason is, in the case that you want to 
put the change code in more that one computer then this will take a lot of time, so with this command we can automatice the process. 
- the module psutil helps to check the percentage of the CPU

### what is version control? 
- VCS Version Control System 
- This help us to keep track the changes that we make to our files
- Here can work one o more persons in the same project
- we can debug in the history of a code to better understod the code 
- We save the code in "repositories", these are like boxes where you can save you code
- We can give access just a part of the code to a differents peoples or grupo of people
- Also we can save text, imagenes, vidos, etc.
 
### Version control and automation 
- for get control in the change git use "commits" to describe the changes and make more easy understand the history 
- if we change the code and the new one doesn't work is more esaly roll back the old code 
- the most comun VCS is git

### Wath is Git?
- scm: sources control magnament 
- is open sources system VSC tool 
- with this tool a lot of people around the world can work together in the same code
- you can use git from you terminal or with the interface
- also you can use the tool as a client or as developer
- like client you can see the code fo the another person and use it 
- like developer you can create you code in another persons can use it
- exist more tool like: mercurial and subversions
- we can pull, push informetion in the git
- they choose git because is the tool more populate

### Installing git
- apt install git
- yum install git
- Git is preloaded with an environment valled MinGW64 (amacias5@DZ-ITDEV4322 MINGW64)
      ----> this environment lets us operate on Windows with the same commands and tools
		avaliable on Linux 

### First Steps With Git 

- we need to say to git who we are: 
	git config --global user.email "me@example.com"
	git config --global user.name "My name"

the flag 'global' set this value for all git repositories that we'd use 

-we have two ways to start to use git
	- git init 
	- git clone

What are the git directory and the working tree? 
The git directory contains all the changes and their history the working tree contains the current version of the files
- we use the command "git add" to add the files that we want to add
- we use the command "git commit" to descirbe or put a note about what you did in the file 
- we use the command "git init" to create a directory of git, this will be empty
	-.git directory alwasy that we clone a repository this directory is copied to our computer

### Tracking files

- Git is compuese for 3 seccions: Git directory, the working tree, staging area
- git directory are: all the change that we made to the files
- the working tree: are the commit that we make to sent the git directory
- stagin area: are the change or modificatios that we are making, like the area of work 
- with "git status" we can see the branch where we are
- with the "git add" we send the change of the file that we want 
	git agg <fileName>
- "git commit -m" the add a coment about that what we made

### The basic Git WorkFlow

- to check out out current configuration by using the "git config -l" command 
- preference we use a different configurations to use a personal account and a work acount 
- we create a ripo with -> git init -> we iniatilice the git but is empty
- if we create a file the file will be untrack "hasta que" we use "git add <FileName> the fiel will be tracked
- we can add massages with the cli or with the editor
- it the commits message is enterted the commit will be aborted

### Anatomy of a commit message
- git log ---> we can see history the command massgae
	- we have here idenfier wich is a long string of letters and numbers
	- head indicator is pointing to the master branch
	- we see the mail and name
	- we can see the date
	- then the massage

### More commands 

Git tracks the changes and displays that the file has been modified. 
You can view the changes made to file using the following command:
git config --global user.name "Name"
git config --global user.email "email@ex.com"
git add <filename>
git status 
git pull
git push
git commit
git diff README

# WEEK 2


- Branches to work on an experimental feature wihout affecting the main code of our project

### skipping the staging area
- git commit -a: shortcut stafe any changes to tracked files and commit them in one step 
- If we're making a small change and want to skip the staging step, which two flags do we need to add to 
the git commit command? Check all that apply. -a -m
- git use the HEAD alisas to represent the currently checked-out snapshot of your project
- one shortcut is skip to the stage are using :
		git commit -a -m "<massage>"
- this shortcut just work with files that already exist becuase they are tracked
- With new files this dosen't work because they are untraked
- The logs work the same way ussing the shortcut, it measn if you see the "git log" then we will see the 
massage of "git commit -a -m "<massage>".
- The head represent in wich branch are you working.

### Getting more information about our changes
- to look at the actual lines that changs in each commit -> git log -p
- here we learn a bunch of commits
	- git log -p: here we can see the log with the changes add, remove lines
	- git add -p: here we can see the changes and at same time we can say "yes or not" to the change
	- git --stat: here we can see the log with the satus of theadd or remove
	- git diff --stage: if we add the changes with this command we can see the differences before the changes tracked
- commit issus: this are when you have a lot of commit and you dont remember what you do \

### Deleting and renaming files
- git remove: remove files
- git mv: rename files
- echo .FILENAME > .gitignore
- if we use commit -m to put a message the massage have to be short, this is just for small changes. 
- ls -la show you all the contente in a directory/repo

https://www.coursera.org/learn/introduction-git-github/supplement/39ZMi/advanced-git-cheat-sheet


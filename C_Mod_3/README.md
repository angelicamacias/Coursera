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
- the syntax is: diff <file1-
 <file2-

- When we use the command diff we will see the symbols -
 < 
	< rest content 
	-
	 add content 
- also we can use the flag -u ----
 "diff -u  <file1-
 <file2-
" this is to get more information about the changes 
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
		diff app1.py app2.py -
		 app_change.diff 
- when we have the file with the output of the change we use the command patch to put the change in the code
	patch code.py < app_change.diff
- if the result is success then we will have just one line the output: "patchin files <namefile-
"
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
- Git is preloaded with an environment valled
	   this environment lets us operate on Windows with the same commands and tools
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
	git agg <fileName-

- "git commit -m" the add a coment about that what we made

### The basic Git WorkFlow

- to check out out current configuration by using the "git config -l" command 
- preference we use a different configurations to use a personal account and a work acount 
- we create a ripo with --
 git init --
 we iniatilice the git but is empty
- if we create a file the file will be untrack "hasta que" we use "git add <FileName-
 the fiel will be tracked
- we can add massages with the cli or with the editor
- it the commits message is enterted the commit will be aborted

### Anatomy of a commit message
- git log ----
 we can see history the command massgae
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
git add <filename-

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
		git commit -a -m "<massage-
		"
- this shortcut just work with files that already exist becuase they are tracked
- With new files this dosen't work because they are untraked
- The logs work the same way ussing the shortcut, it measn if you see the "git log" then we will see the 
massage of "git commit -a -m "<massage-
".
- The head represent in wich branch are you working.

### Getting more information about our changes
- to look at the actual lines that changs in each commit --
 git log -p
- here we learn a bunch of commits
	- git log -p: here we can see the log with the changes add, remove lines
	- git add -p: here we can see the changes and at same time we can say "yes or not" to the change
	- git --stat: here we can see the log with the satus of theadd or remove
	- git diff --stage: if we add the changes with this command we can see the differences before the changes tracked
- commit issus: this are when you have a lot of commit and you dont remember what you do \

### Deleting and renaming files
- git remove: remove files
- git mv: rename files
- echo .FILENAME -
 .gitignore
- if we use commit -m to put a message the massage have to be short, this is just for small changes. 
- ls -la show you all the contente in a directory/repo

https://www.coursera.org/learn/introduction-git-github/supplement/39ZMi/advanced-git-cheat-sheet

# Week 2

- Branches to work on an experimental feature wihout affecting the main code of our project

## skipping the staging area
- git commit -a: shortcut stafe any changes to tracked files and commit them in one step 
- If we're making a small change and want to skip the staging step, which two flags do we need to add to 
the git commit command? Check all that apply. -a -m
- git use the HEAD alisas to represent the currently checked-out snapshot of your project
- one shortcut is skip to the stage are using :
		git commit -a -m "<massage-
		"
- this shortcut just work with files that already exist becuase they are tracked
- With new files this dosen't work because they are untraked
- The logs work the same way ussing the shortcut, it measn if you see the "git log" then we will see the 
massage of "git commit -a -m "<massage-
".
- The head represent in wich branch are you working.

## Getting more information about our changes
- to look at the actual lines that changs in each commit --
 git log -p
- here we learn a bunch of commits
	- git log -p: here we can see the log with the changes add, remove lines
	- git add -p: here we can see the changes and at same time we can say "yes or not" to the change
	- git --stat: here we can see the log with the satus of theadd or remove
	- git diff --stage: if we add the changes with this command we can see the differences before the changes tracked
- commit issus: this are when you have a lot of commit and you dont remember what you do \

## Deleting and renaming files
- git remove: remove files
- git mv: rename files
- echo .FILENAME -
 .gitignore
- if we use commit -m to put a message the massage have to be short, this is just for small changes. 
- ls -la show you all the contente in a directory/repo
https://www.coursera.org/learn/introduction-git-github/supplement/39ZMi/advanced-git-cheat-sheet


## Undoing change before committing

- git checkout : git checkout <filename-
 with this command we rollback to the last version of the file if you dont want the changes that we made. This is before be in the storing area it means is not commited 
-git reset : if you add a change to the stage area but you dont want that, then with the rest you can reverte the commit,
-with git reset -p: git will ask change by change if you want to reverte the commits that you made
-git reset is the antonimus of git add|| remove changes from the stagin area
-head alias: current checked out snapshot

## Ammending commits

-git commit --amend: update the commit to include the new change.
    It wil take whatever is currently in our staging area and run the git commit workflow to overwrite the previous commit.
-when you use the --amend commant it will let you change the massage and will add the new changees
-remember the fist line short and de second line a litter more descriper
-so git commit --amend: Overwrite the previous commit
-this commit its ok for fixing up local commits
-if you use it in public or shared repository rewrites the git history removing the previous commmit and replacing it with the ammended one


## Rollbacks

git revert t creates a commit that contains the inverse of all the changes made in the bad commit in order to cancel them out

syntax: 
git revert <HEADER->


- We will see that in the commit by defult willbe added a line indicate that is a rollback 

- When you do a rollback ists a good idea the reason about why do you do a rollback? add in the commit

- the output of git revert and git commit look "parecido" that is because git revert create a commit for us

- git log -p -2: lets us see the patch created by the commit while the dash two the last two entries

## identifying a commit 

-the characters next to the word: commit is the ID, or HASH 
-the HASH is calulated using an algorithm called SHA1
-Essentially, what this algorithm does is take a bunch of data as input and produce a 40 character string from the data as the output.
 example: commit a05ee5d184e9a21259e3fdc53eda01649348359e (HEAD --
  master)
-the HASH is used to: used to guarantee the consistency of our repository.
-the commit --amend change the HASH for that is not good use it in a public repo
-git show <HASH>
  then you will see the author, date and massege commit
 -git revert <HASH>
  can but with jus the 4th first characters

# Week 3
## What is a brancH? 

Branches make it really easy to experiment with new ideas or strategies and projects. When you want to add a feature or fix something, you can create a new branch and do your development there. You can merge back into the master branch, when you've got something you like, or discard your changes without negative impact if they don't work out

- the master branch is the prod proyect
- we create a branch to create changes next to the proyect of master
- if we are sure that the new content wont make mistake we can add the content to the master branch
- Exist strageri of branches

## Crating new branches
- git branch: show us all the branches in the reposityory
- git branch <new_branche>: we can crate a new branche 
- we can be in the master branche an create a new branche, but when you see all the branches with "git branch" we gonna see **master\*** 
- git chechout: the lastest snapshor for both files and fro branches
- git chekout <name_brnache>: with this command we log in to the brnache
- git checkout -b <new_branche>: we create and log in to the new branche

## Working with Branches
- Remember that when we switch branches, git will also change files in our working directory or working tree to whatever snapshot head is currently pointing at.  
- at the current contents of our directory.When we check out a new branch and commit on it, those changes will be added to the history of that branch. 
-One thing to note after all this back and forth, is that each branch is just a pointer to a specific commit in a series of snapshots.
-How does git checkout switch branches?By updating the working tree to match the selected branch.
-git branch -d: So what if we want to delete a branch that we don't need anymore? We can do that by using git branch dash d.

## Merging

-git merge <branch_name>: put the contenten in the branche
- merging: this is when the content of some branches combing data and history togeher
- exist two froms to work with merging
- fas forward: the master branches is update with the merges
- three way: you create a branche then when you add the content git commit the change 
- merge conflit: an exmple is when some files are modify in a branche, and same files are modify in another branches... then git hub wont know wich changes is the correct
- git log --graph --oneline:
```
*   22194ff0 Merge branch 'puppet-dev' of https://gitlab.autozone.com/10550551/puppet into puppet-dev
|\
| * fb300bed crm - 780 change the fact: az_oel_info_077_comm_driver
| * 59b92b7c delete comment
| * fe35ea44 rollback to the last version of the class
| * 6091291d CRM-781 remove the json files
* | b0b6a8a1 CRM-771: az_rollback_firefox_policies_json
|/
* d2c
```
with command show you a graph of the commits 
- We will learn how to track and untrack merges to the staging area
- Work with remote respository is super helpful becasuse you can work with people to differents contrys 
- We will lear how to made changes changing to branches


## What is GitHub?

- **Distributed**: Each developer has a copy of the whole repository on their local machine
- gitlab is a remote repository hosting serive 
- you can create privete or public accounts
- in gitlab also you can put wikis, mangnemetns task... etc
- in git lab you can put the documents and then you can clon in you local machine or syncronice with some other servers, is the way that a team can have the same documents. 

## Basic interacion with GitLab

- first we have to create an accunt 
- in the account we can create the fistr repository
	we can select if the repo will be: private or public
	and add a redame 
- to have the same content in our lcal machine we use the commant: git pull 
- to remove the password step we have two options: credential or the ssh key
- git config --global credential.helper cache: command to create the credential for git ---> Allowing automated login to GitHub
- also exist another plataforms like: gitlab or bitbucket 


## Whast is a remote? 

- With a remote repo all the people who have access can have a copy in their local machine.
- When we work with remote repositoris with a team is recomend chang the steps, like the marge will make manualit to approve the changes
- We can control the access to the remote repository with differents way like: 
	- ssh key
	- https
		methods of autentication 
- When the remote repository have new changes, and you want to push your changes... git will tell you that you have to update you repo in you local:
				git pull origin <header>

- in the case that a file was changed for two people we will have a conflit merage.. 


## Working with remotes
- Pull the remote branch, merge it with the local branch, then push it back to its origin.
- Git sets up that remote repository with the default origin name
- git remote show origin: show a lot of information about the branches
- git branch -r: show us the remote branches 
- git remote -v :  We can look at the configuration for that remote by running git remote -v in the directory of the repo.


## Fetching new changes
- git fetch: To sync the data, we use the git fetch command. This command copies the commits done in the remote repository to the remote branches, so we can see what other people have committed. Let's call it now and see what happens.
- git merge origin/master: If we want to integrate the branches into our master branch
- Whats the main difference between git fetch and git pull?
	git fetch fetches remote updates but doesn't merge; git pull fetches remote updates and merges. 

## Updating the local repository 

- git pull: this comand do fetch and mergin  Running git pull will fetch the remote copy of the current branch and automatically try to merge it into the current local branch.
- assuming no merfe conflics, which type of merge does git pull perform automatically: 
	fast-forwar merge
- git remote show origin: if we need to fin more infromation about a remote branche
- git remote update: get the contents of a remote branch without automatically merging 
- explicit merge: creates a new merge commit

## Rebasing your changes

- git rebase: tebasing menas changing the base commit that's used for our branch
- git rebase helps to hae a cleanly integrate commit
- git push --delete <branchName>: remove the remote branche
- git branch-d <branchName>: remove the local branche
- the git rabase helps to put your commit at the top and avoid git conflicts
- we want to our changes are lines we can see the flow of the git with: 
git --graph --online
in the case that we have a branch with commits and at the top we have a commit... for put at the top our changes we use: git rebase  
What does "git rebase refactor" do?
	Move the current branche on top of the refactor branch

## Another rebasing example
The socket module: The 'socket' module defines how server and client machines can communicate at hardware level using socket endpoints on top of the operating system

- socket.gethostname() returns the host name of the current system under which the Python interpreter is executed
- We can also use the use git rebase to change the order of the commites or even squeash two commits into one. 

## Best practices for collaboration 
- Always synchronize you branches before staring any work on you own 
-Avoid having very large changes that modify a lot of different things 


https://git-scm.com/book/en/v2/Git-Branching-Rebasing

# Week 4
## Collaboration 
- With tools like giHub we can publish our code and you can see the code of the other people 
- At the same time you can have that code in your local and in the case that you found some bugs or you have some suggestion you can comment about it in the repo
- Having the code published online means that anyboday in the world can lear form what the project is doing. 
- Also we can create a prive repo where just your and the people that have access can see what the project is doing. 

## A simple pull request on GitHub
- fork: a fork is a copy of some repo in your local. 
- you can make changes in the fork and then send the changes to the master branch 
- When you dont have access to the master branch and you want to fix some issue automatically gitHub will create a branch  to send the fixes that you made.  
- pullrequest: a pullrequest is a commit or series of commits that you send to the owner of the rpository so that they incorporate it into their tree. 
- when you create a pullrequest we can see in the UI a lot of information about the PR: repo and branches that are involved in the change.
- When collaborating on projects hosted on GitHub, the typical workflows is:
	1: Create a fork of the repo
	2: Work on that local fork 
	3: We wventually merge  our changes back into the main repo by a pullrequest

## Updating an existing pull request
-  Immpruvment: documentations or test. Some times the team of the project can ask for immpruvment to approve the change request. 
- commit same branche. If you send a merege request... and then you send more commits all the new commils will go to the same branch. 
-If we wanted to create a separate pull request, we would need to create a new branch instead
-Github renders our file and highlights the changes. 
- In the UI of GitHub we can see the add lienes in green and the delete lines in red.
- Some time in a project can exist guidelines that we need to follow to can send a merge request, it's important to adhere to them to have a style and all can undertan more is whats going on. 

## Squashing changes
- We shouldent rewrite history when the commits have been pusblished


## The typical pull request workflow on GitHub
- For makw large change and testing is a best practice create a fork in our repo
- When we have the fork in our repo, we will have the current files and the history about the repo
- After that to work in the repo we can clone the fork with: git clon <ssh/htpp> 
- Having the repo cloned in our local we can make the fixes, also with git log, we can see all the history about the fork 
- All the issus have a identify number which we can access to the issue like: #1
- README: means MD extenstion indicates that we're using markdown, which is a ligthweight markup language. 

## What is a code reviews?
- Code reviews helps to check the content of the new code fix:
	- Bugs
	- Style
	- Unclear variables or functions
- In the case that you are working with a remote team exist diferents tools for the do codereviews
- Code Reviews give us a feadback about the new contentent. 

## The code review workflow
- The workflow for code review is:
	- create the code
	- send the code to review
	- If you have a feadback then they will send you the code to fix that problems wiht comments can be:
			- suggestions
			- bugs
			- testings
	- then when you have the fixes then you send again the code, then you approve the contente the contente can be push the re repo 
- in the case that you are working with a team is recomended ask for a style to follow in the creation of the new contente
- some lenguajes have the own rules like python: PEP8 
- nit: is a trivial comment or suggestion 

## Managing collaboration 
- It's very important create a documentation about the proyect for:
	- In the case a some guy of the team go to vacations
	- In the case a some new guy will integrate to the team 
	- To understand better how the proyect works 
	- In the case that you have a style for the creation of new content, have it in the documentation it's helpfuly to hava a guie about it.
	etc

- It's very important have a comunaction with the team we can use some tool like: 
	- Slack
	- Telegram 
	etc
- It's important undertand every merege to know if you can or not acept it, because if you acept every merege without undertand what going on, then the proyect could be unmaintainable.

## Tracking Issues
- coordination: its important defined who will do what, for the moment that all the work will be together all the problems can be solve wiht an efficent way.
- issue tracker: this tells what issue needs to be done and who will work on it
- in git lab we can track the issue with comment of the new contente an we can assing who will work in that issue
- When writing issues descriptions, it's a good idea to include all the information that we have about the problem or missing features and any ideas on how to solve it. 
- a puplar bug tracker is: Bugzilla
- The READMES can help to put the descirption about how to use some program or whatever do you want. 
- The tack comment also have a id like the commits.
- How do we reference issues in our commits with automatic links? By using one of the keywords followed by a hashtag and the issue number

## Continuous integration 
-CI: continuous integation, in this part make differents testing of the code hoping the result is that we want. 
-CD: continuos delivery: this point happen when the part of CI is succefuly, the new content is diployet in the server.
- GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform available through GitHub.
-PIPLINE: the pipline is the steps that you want to evalute to know if is correcto the new code, we configurate the pipeline in a YAML format. 
-Artifacts: this is the name used to descirbe any files that are tenerated as part of the pipline. 
- It's importat to identify in which area the piple will work, to not compromise another environment. 
- Also its important give access just to the people how can work in that area or in that piplines, we can give acces with:
	- SSH key
	- API token
- The piplines are a greate opportunity area because every project have different needs, different tests and creteris to evaluate, having the notions about what is important to evalue and how can we create a robust pipeline we can create a estable pipeline. 
- Also another plataform to CI/CD is Jenkis wich can bu used to automate lots of differents types of projects. 
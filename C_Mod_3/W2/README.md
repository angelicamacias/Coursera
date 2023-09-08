

- Branches to work on an experimental feature wihout affecting the main code of our project

~~~> skipping the staging area
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

~~~> Getting more information about our changes
- to look at the actual lines that changs in each commit -> git log -p
- here we learn a bunch of commits
	- git log -p: here we can see the log with the changes add, remove lines
	- git add -p: here we can see the changes and at same time we can say "yes or not" to the change
	- git --stat: here we can see the log with the satus of theadd or remove
	- git diff --stage: if we add the changes with this command we can see the differences before the changes tracked
- commit issus: this are when you have a lot of commit and you dont remember what you do \

~~~> Deleting and renaming files
- git remove: remove files
- git mv: rename files
- echo .FILENAME > .gitignore
- if we use commit -m to put a message the massage have to be short, this is just for small changes. 
- ls -la show you all the contente in a directory/repo
https://www.coursera.org/learn/introduction-git-github/supplement/39ZMi/advanced-git-cheat-sheet


## Undoing change before committing

> git checkout : git checkout <filename> with this command we rollback to the last version of the file if you dont want the changes that we made. This is before be in the storing area it means is not commited 
> git reset : if you add a change to the stage area but you dont want that, then with the rest you can reverte the commit,
> with git reset -p: git will ask change by change if you want to reverte the commits that you made
> git reset is the antonimus of git add|| remove changes from the stagin area
> head alias: current checked out snapshot

## Ammending commits

> git commit --amend: update the commit to include the new change.
    It wil take whatever is currently in our staging area and run the git commit workflow to overwrite the previous commit.
> when you use the --amend commant it will let you change the massage and will add the new changees
> remember the fist line short and de second line a litter more descriper
> so git commit --amend: Overwrite the previous commit
> this commit its ok for fixing up local commits
> if you use it in public or shared repository rewrites the git history removing the previous commmit and replacing it with the ammended one


## Rollbacks

git revert t creates a commit that contains the inverse of all the changes made in the bad commit in order to cancel them out

syntax: 
git revert <HEADER>

- We will see that in the commit by defult willbe added a line indicate that is a rollback 

- When you do a rollback ists a good idea the reason about why do you do a rollback? add in the commit

- the output of git revert and git commit look "parecido" that is because git revert create a commit for us

- git log -p -2: lets us see the patch created by the commit while the dash two the last two entries

## identifying a commit 

>the characters next to the word: commit is the ID, or HASH 
> the HASH is calulated using an algorithm called SHA1
>Essentially, what this algorithm does is take a bunch of data as input and produce a 40 character string from the data as the output.
 example: commit a05ee5d184e9a21259e3fdc53eda01649348359e (HEAD -> master)
> the HASH is used to: used to guarantee the consistency of our repository.
> the commit --amend change the HASH for that is not good use it in a public repo
> git show <HASH>  then you will see the author, date and massege commit
 > git revert <HASH> can but with jus the 4th first characters
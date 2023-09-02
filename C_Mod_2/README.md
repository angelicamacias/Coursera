
# Week3

### Wildcards and character classes

- With the function re.search we just find the fist incident 
- With the function re.findall we find all the incidnets 
- We can use [] to put the range of characters we want to find 
- We can use ^ to exclude the characters we dont want to find--- [^a-Z] or [^0-9 ] includin the spaces. 
- We can use | we finde one thing or another like cat|dog (cat or dog) 


### Repetiton qualifiers

- with .* we can fine all the ocurreces includin a-z and 0 c.*t ----> cadsdffsdt csd0t
- also we can use [a-z]* to find all the incidences of the range a-z, but here spaces and symbols aren't inclucd
- like grep with ? we can assing to cero or one value like c?t---> cat c9t c!t at
- we can use + to search more that one time like [a+] --> caat caaat
- Also we can do this [a+l+] to search the letter a and l with 1 or more incidence but the same patter, nothing between them 
- in the programtion exit the term "greedy" that means the searech more complex 

### Escapting characeters

- We can use \ to escape special chacracters 
- In paython exist methos like \d, \w \s ans this are using to special sentences
- exist a plataform regx. somthing to play 
- the use of the methos... are like a game of words i mean 

	for do mantching of this santence: caT  eat  f00d 
					    \w\s+\w 
so dependign of the santence that we are looking for you can use the sepcial methos of matching


### Regular expressions in Action 

- bewteen the [] we put all the content that we acept in some part of the sentences, 
- again we can use + to say "one or more incident of the characters that we search or the 
content bewteen []"

### Captuing groups 

- We can use () for grupoing search that means in one search in place to just look for one patter, we can search 
	two pattern, this is named "capturing groups"
- We can manipulate the output of "capturing gruops" like a index with 0 we will get all the output
	with 1..2..n each value of the output
- The same form we can give format to the index, like: {}, {}.format( [1], [2])
- We can use the method grupo and this will give us a tuple, we can manipulate the tuple to create our format 

### More on Repetition Qualifiers

- the repetiton qualifiers detemin how many time do are looking for a patter
- to use the repetition qualifiers we use {} 
- we decide how many incidences acept like {7} 
- we can decide a range de incidences {5,9} 5 to 9
- we can use the comma to say {,5} words up to 5
- we can use the comm to say {7,} more that 7 incidences 
- the \b is to search the exact match 

# VWEEK 4

### Standard Streams

- here we saw the wey that the system is comunicating, with o/i
- the stedrr is for standar erro: for errors
- stdin standar input: for enter information 
- stdout standar output: for out infromation 
- we can manipulate the data

### Environment Variables
- Environment variables are variables that are declare in the opatin system
- to the the contnte of the varible we use the command echo and and $ is menas: echo $VARIABLE, THIS IS IN bash 
- we will work with shell, is a interfece to the operatin system
- we will use bash, but the same way existe another version like fish and zch 
- in python we can use the os module to have acces to the conten of operation system
- we use os.environment to have acces to the environment variable and the method get to have the 
  content of the vaible: os.environment.get(VARIABLE )

### Command-Line Argument and exist stauts

- cli are parameter that we can pass to run the script --> python arg.py ar1 ar2
- we use the sys module to can use the comand line in this way : sys.argv
- if the code run successfuly we get an exit code 0
- if the code dont fun succesfuly we will get an exit code 1
- the same way to use the exit code we have to import the model sys --> sys.exit
- in general the exit code help us to know if the code run with success or not
- 0 is success and wherever number that dont be 0 is an error
- wc this command tell us how many lines, words and chracter are in the parameter that you pass

### Running system commands in python 
- here we learn about parent proces... we see that when a command is executing into a "program" 
  create a child process before the child process and the parent process continus. 
- to work with the process we use the method subprocess: subprcess.run(["date"]) with the parameter
  run we tell to python that run the command into the []
- we can see the exit code: result.returncode

### Obtaining the output of a system command 
- here we saw how to capture the stdout and stderr 
-  print(result.stdout)
b''
for this the b means byets, the character that is create any data 
- we can manipulate the stdout and stderr
- here mencioned about the command who, this is to say the currtly host 

### Filtering log files out of the data
- is better read a file that is to large with a for loop line vy line
- the key word continue meeans "go to the next element"
- we saw how to escape character
- we can use the $ for have a match to the end of the expretion 
- + help to say "one or more time"
- a crontab is the way to schedule a task 

### Making sense out of the data
- A greate way to count how many time appere a log we can use a dictionari 
- the method get helps to have the infomation that we are looking for 
- we can use the key None to chake if the variable is none


# WEEK 5

### What is testing? 
- Testing is prove your code to look for a bugs 
- Exist differents types of test 
- Exist test manual and automatied test


### Manual testing and automated testing
- we can do a manual test pasing differents parameter to program and see what happen 
- we can automate the manual test for the program can do differents things with differents parameters
- When we say "automatic testins" means that the same code do it. 
- the goal of the automate testing is that the parameter match with the expetation 
- is better auomate the testing for the time and the test if the code is good we will get the expected results
- we will learn about the unit testing

### Unit tests
- Unit test is make a test just an isolate small part of the code 
- Unit test have the  avantage that is fast and easy to debug 
- in the entrepice word exist hte "test environment" where we can put the our ruls to make testing 
- but we are looking for do this testing automatically 
- unit test are usually written algon of the code like a functions or methods

### Writing unit tests in python 

- Exist a moduel that provides class to create testings: unittest
- the method self.assertEqual help to verify if the arguments are equal
- for the testing we have to create another file with the same name of the code that we are tesing but 
with the prefix _test for convections
- with the key word from we can import from the original code the function that we want to test
- we can prove our testing calling the function unittest.main()
- the output give us the time and the number of testing that we are doing 
- Any method we define in out TestRearrange class that start with the prefix test will automatically 
become tests that can ve run by the testing framework. 
- the function have to start with the word "test" for impement the unittest

### Edge Cases
- Edge cases are expections of the limited of the code can work, this means cases when the expected argument is totaly different that we expext
- For edge cases we can create a scritp into the code, that help that the code continue runing 
- Edge cases are all the imaginarie situacion that we can pass to the code that dont be that we are expected

### Additional test cases

- we need to think about all of the posibles options for the test
- the avangae of do this is that we need to do a script for each posible case
- asertionError: '' != Billy , this is because we have an empty string in place of the expecte value
- the function have to 
- method called setUp(), which the testing framework will automatically call for every single test we run


#### Notes: 
The test module can be run standalone from the command line.
The test code can more easily be separated from shipped code.
There is less temptation to change test code to fit the code it tests without a good reason.
Test code should be modified much less frequently than the code it tests.
Tested code can be refactored more easily.
Tests for modules written in C must be in separate modules anyway, so why not be consistent?
If the testing strategy changes, there is no need to change the source code.

### Black box vs White box
- the white box is when you know how the code works and for that you can do test knowing what expect the code
- Bkack box is opate, because you dont know anything about the code, you just try to use it 
- The two type of box are usfuel, because with the wihte box, you know what tyep os test you can make, but 
in the other hand wiht black box, you need to try to undertand how the code work... like if you down a new game. 
- black box: verifies that the details for a producto 
- with box: verifies differents functions in the code 

### Other test types
Running a piece of software code as-is to see if it runs describes what type of testing: smoke test
- smoke test: verify that the code run... but without any change, like a calish
- load test: to see if the code soporte a lot of request 
- regrestion test this test make sure that the same mistake dosen't happen twice
- integration test verify that the interactions between the different pices of code in intetrated envvironments are working the 
way we wcpected them 
- having integration tests will help make sure that all pices come together the way you expect them to 
- taking together a group of test or one or many kinds is commony referred to as a test suite
- if we use more and more test we will get a rebust test suite

### test-driven development
- we generaly make the code and then make the test
- TDD test driven depelopment, this is the prcen where you make fisrt the test and then the code 
- Do tdd helps to anticepetd the problems and the code and have more certine about what are you looking for you code 
- A lot of companys do this to be set fruther at the moment you put your code in de repos
- continues integrestions is when your code put on the repues and the tests are made automatically to stops bugs and erros 

### The try-except construct
-  the try-expect helps to try first  the option that you want, 
- if the try make an error then the expetion is retun
- this make more easy and short code

### Raising erros
What keyword can help provide a reason an error has occurred in a function? assert
- here we saw the key words raise and assert
- raise: this helps to raise an error ourselves
>>> The raise statement allows the programmer to force a specified exception to occur.
- the raise key word helps to create owns error in case that the result dosent has sense 
- asert: helps to alert what type of output we wait
- asert have to be remove in our code if we want that the code be faster
>>> assert condition
... you're telling the program to test that condition, and immediately trigger an error if the condition is false.
Do not use parenthesis to call assert like a function. It is a statement. If you do assert(condition, message) 
you'll be running the assert with a (condition, message) tuple as first parameter.
- isalnum method is dosent work for a list
- we have to close the pyton terminal and agine open to use the modifications in our code 

### Testing for Expected errors
- the test suits are the grupo of tesing of a code. 
- we can add the rasing error with the method assertRaises that provide the module unittest
- the asserRaises helps to work with the invalid parameter
- the assertRest work with a "try"
- we have to pass first the error, then the name of the function, and the parameter that need that function 


# WEEK 6

### Redirecting streams
- 0 stdin is all the data that pass to the keybord to terminal and some comands
- 1 stdout is the output that generte each successful command
- 2 stderr is the error output that generte each command
- the redirections helps to put data into a file
- > this simbole put the content that you want into a file, but this eliminate all into 
the file, the content that will be there will be the new
- >> this appen the new content in the file
- we can use 2> to redirectioner the errors into a spfecific file
- and this < helps to redrection but backwards---> ./scirpt.sh < new_content.txt
	redirect content to a script

### pipes and pipelines
- the pipes helps to connect commands
- the output that the command helps to the another
- the character is |
- with the module sys we can work with the srteams (stdn, stdo, stderr)
- cat haiku.txt | ./capitalize.py with python we can parsh some gaps to the use the pipe in bash 
- the uniq command helps to see especific incidentes of that we want to see
- head print just the 10 first lines
 
### sinfnalling processes
- Signals are tokens delivered to tunning processes to indicate a desired action 
- we can see the singles of with the command ping
- SINGINT we can use ctrl + C to finish the command ping, then we will get a resum of the information 
- SINGSTOPEwe can use ctrl + Z to finish the command ping but it will just intrrupe the process continus.
- if we want to still watching the process we can use the command fg 
- kill -> SIGTERM this helps to kill the process that we want 
- pid means proces id, the number with we can identifie a process
- ps ax --> running processes in the current computer
- ps ax | grep <pid> the process will just stop. 

### creating bash scripts
- we can create a script in bash when we want to run a lot of commands 
- the free command show the space in the computer
- the uptime show the time that the user use the sesion 
- to use the output of some command we need use this sintax --> $(command)
- we can use enter or semicolon to separete each command

### Using variables and globs
- for use the glob in pytho we need to import the module globs
- globs helps to do match with something that you are seaching
- the * search wherever the caractes be
- the  ? search just one character
- the syntax of the variables is ${variable} 
- to declare a variable we dont have to use spaces VARIABLE=DATA

### conditional Execution in bash
- exit status tell if the program was successfuel or not
- is nice use identetion but is not a rul 
- we use the if, then, else keywrods
- grep command work like a filter of the informetion that we want
- we use if <command>; then here we need to use ; but in the same way we can use
   if <command>
- the command test we can use to define the condtion or in place we can use [[ ]] 
- [] is an alias of the command test

### While loops in bash scripts 
- the while loop work until the condition be true
- the syntax is: 
	whiel <condition> do
		<condition>
	done
- remember to we can use arg in bash $1 with this way
- the random moduel helps to give us numbers randomly with the 
- with the sub metho randint we can give to the moduel random a range of int 
- we can manipulate the exist status in this way sys.exit(<variable>)

### For loops in bash scripts
- in python data sequences are: tuple, strings, list
- in bash we contruct sequences just by listing the elements with spaces in between 
- the command basename parte the(in this case) the file name subtrea the extencion name: 
	$basename perro.html .html 
	perro
- like a tip use the echo command to seee what we will do, in this case we will work with the file system 
 so, we need to have more carfuel to the error, so this work like a chalish 
	
TEST:	echo mv "$file" "$name.html"
REAL:	     mv "$file" "$name.html" 
- A for loop is the way to iterate a sequence 
- the syntax is: 
	for <variable> in <sequence>; do 
		<conditions>
	done
- we can use the wildcards helps to list file with incognit characters

### Advanced commands interaction 
- the system log file is located in var/log/syslog
- the syslog conteint a lot of information about what going on in the computrer
- tail show the last 10 lines in a file
- cut let's us take only bits of each line with a delimeter 

### Choosing between bash an python 
- when write in bash be to dificult

$ cat story.txt | ./capitalize_words.py
- but if your code is complex or it needs to work across platforms, you might be better off using the Python standard library or other external modules that provide the same functionality.

### STEP FOR CODING PROJECTS
- Undertand the problem statment
- Research 
- Planning
- writing
- testing


regex101.com


two parameter: 
- the name of the CSV file to read
- the name of the HTML file to generate
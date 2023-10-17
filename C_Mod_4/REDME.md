In this course, you’ll learn how to debug and troubleshoot a wide range of technical problems, both in your code and in someone else's code.

Course prerequisites
This course requires some familiarity with basic IT concepts:

- Operating systems: file systems, processes, log files

- Computer hardware: CPU, RAM, disk, graphic, and network cards

- Basic networking: network connections and network bandwidth

The example scripts and programs in this course are written in Python, so you’ll need an understanding of this programming language, too

# Week 1 Troubleshooting concepts

## What is debugging?

- troubleshooting is the process of identifying, analyzing and solving problems. 
- Debugging is the process od identifying analyzing and removing bugs in a system
- Exist some linux command that give us information about the system like: top, free etct
- the strace to look at the system calls made by a program command help us to see what going on in the system.
- tools to duebug tcpdump and wireshark
- we nned tod undertand why and figure out how to solve a probelem 

## Problem solving steps

- to solve the problem we have 3 funtamentals steps but don't always is the same flow 

- information: getting information about the problem, read wikis, or docuementations, even ask in interntet. 
    reproduction case: this means.. when is this happen? 
- finding the root couse: what is the factor that provocs this issue? 
- Performing the necessary remediation:  this means what is the necesry that we can do to redic with the issue.
- we can solve the issue for the momment enough to create a "workaround"
- workarounds means lets our users get back to work quickly
- sometime we need to solve the problem quickly but it dosen't means the problems is readicate, sometime we need more time to undertand what we can do to priven this issue come back. 
-long-term remediation: make sure you get notified early when they're overheating , and also include checking if you can reduce the probabilitys of the issue

## Silently crashing application
- information: like we mencioned first we need more information about the problem 
- reproduce the same issue in own computer to analyze what going on 
- strace: the stace command show us which system calls are calling in the karnel shell 
- system calls: calls that the prorams running on our computer make to the running kernel
- strace -o  faliure.strace: the command strace with the flag o generate a file with all the contente generated by the command strace
- less <filename>: this comman give us the last contente of the some file 
whit the next example: 

```bash
~$ strace -o failure.strace ./purplebox.py
~$ less failure.strace
## the important line is:
openat(AT_FDCWD, "home/user/.config/purplebox", (O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = -1 ENOENT (No such file or directory)

```

- openat: to open files or directories the content of the call shows the parameters passed including the path(home/user/.config/purplebox) that's being opend and a buch of flags 

- the O_DIRECTORY flag tell us that the path is being opened as directory, the nomber after the equal sing shoes us the return code of the sys calls
- immediate remediation: is tell to the user that he needs to create the directory
- in this case long-term is: is tell to the developer that his release have an issue and meaby he will need another version about it. 

- the last step is actualizce the documentation with the new infromation 

which command can you use to scroll through a lot of text output after tracing system calls of a script? 
strace ./script.py|less
Which tool can you use when debugging to look at library calls made by the software? the ltrace tool is used to look at library calls made by the software.

## It dosen't work

- to undertand what is going on with the issue we can ask:
What were you trying to do? 
What steps did you follow? 
What wat the expected result? 
What was the actual result?

and go:
it doesn't work
to :
when i tried to log in, the page keeps leading and never shows the landing page

-  top command: shows the sate of the computer and processes using the most CPU and see that the computer is super overleaded 
- the load averge on linux : shows how much time a processor is busy in a given minute
- when the process are stuck waiting for the operating system to return from system calls usually happens when processes get stuck gathering data from the hard drive of the network. 
- we can see all the process running and see which sistem is using a lot of system calls, and maybe kill that process
- it's important try to replice the same issue in you own computer to undertand what is happening 

## Creating a reproduction case
- create a repduction case helps to understand better what happen when the issue comes. 
- something that we can do is see the logs after try to replice the same issue we can see the logs in: 
     Linux: /var/log/syslog
        user-specific:  the.xsession-errors 
    MacOs: library/logs
    Windows, you'd use the Event Viewer tool to go through the event logs. 

## Finding the root cause

- Understanding the root cause is essential for performing the long-term remedition 
-Whenever possible, we should ckeck our hypothesis in a test environment, instead of the production environment that our users are working with 
- generally, undertanding the root cause is essential for providing the long-term resolution 
- iotop: which procees is generating a lot of input and oupur
- iosatr and vmstat: 
- ionice
- iftop: shows the current traffic on the network interfaces
- nice: reduce the priority of the process and accessing the CPU
-IN CONCLUSION YOU HAVE TO USE THE ALL YOUR IMAGINATION AND COMPRUBE ALL THE HIPOTESYS THAT YOU HAVE

## Dealing with intermittent issues

- actually exist some tools to debug mode in differents systems 
- if you can conut with that tools to debug we can think on:
    - the load on the computer
    - the processes running at the same time
    - The usage of the network 

- oserver effect: observing a phenomenon alters the phenomenon 
What sort of software bug might we be dealing with if power cycling resolves a problem?  Poorly managed resources

## Intermittenly failing script
- zenity (program meeting_reminder.sh) is a progam who show in the windo select... title, date, and another information

## What is binary search? 

- linear search: liner serach is when you search in a list line by line
- one of the problem for longer search is that when the list is to longer we will spend more time seaching line by line
- the binary search helps us to search depending in how to big is the line that are looking your
- to create the alogritmo of vinary search is very importan relize the sort funcion first, because we need to have up or down the most begger digito or characters that can looking for
- the binary search skeep for seccinos descart the seccions depending in the character or digitos that you are looking for 


## Applying binary search in troubleshooting
- bisecting: this means try to divide the total of problemes that you have, it means if you are working with 12 files and you dont know where is the problem to find more quicky in place to search file by file we can prove with the first 4 files looking for the error, with that in place that have 12 steps we will have 3 steps
- in the case that we have an xtml file and we want to find the error we can bisect in function of the variables that are there
- git bisect: in the case that you have a versio control VC like git we can use the command git bisect to find the command that created or introduced the error or bug
- bisecting the problem help us to reduce the iteraction to find it 

## Finding invalid data

- head: command head give you the first lines of a file
- tail: give you the last lines of the file
- |: help you to connect command in bash 
- the long-term: try to figure out which is the cause of the problem
- short-term: fix the problem yourself to continue with the work 
- the flag --server: helps to pass the test as the arameter 
- in the case that we what to bisect a file the comand head, tile and the character | can help us a lot. 

# Week 2 Slowness

## Why is my computer slow? 

- Sometimes our computer is slow because it donesn't have enough resources in this disponetion, maybe we have a lot of pages open 
- top: this command let us see: 
    - which currently running process are using the most CPU time
    - Which process are using the most memory 
    - how many processes are running 
    - how the CPU time or memory ir being used
-iotop and iftop: this comand can help us see which processes are currently using the most disk IO or the most network bandwidth 

## How computer use resources
- cache: Stores data in a form that's faser to access than its original form
- web proxy is a form of cache it stores:
        - websites
        - Images
        - videos
- When you are using some program it will be in the ram memory
- The program that wont be using will be stored in the disk memory
- swap: swaping refers when the process leap between ram memory and disk memor
- memory leak: memory which is no longer needed is not getting released 

After retriving data form network, how can an applications access that same data quicker next time? 
        Create a cache

## Pssible causes of slowness

- A computer becomes sugglish after a few days, and the problem goes away after a reboot. Which of the following is the possible cause?
    A program is keeping some state while running
- we can have some posibles reasons to have a slower computer 
-  We can have some possibles resons to have a slower computer the recomendations is go to the easy possibilities to the more dificult, this help us to descart some of them 
- Sometimes when our computre started slow can be becase we have a lot of application that started at the same time
- Another posibilitie case can be that the program sorte data on memory without delteing the old data
- Also can be program with large files, for this case we can try to reduce the size
- To reduce the size we can use: lograte tool
- We also can hava maliciouse program in our computer that provoce the slower actions. 

## Slow web server
locate -> 
grep ffmpeg*
deamonize : run each separli 
killall -STOP <processName>
sleep: 


for pid in $(pidof ffmpeg); do while kill -CONT $pid; do sleep 1; done; done

ab -n 500 

## Writing efficient code 

- To create a efficiente code help to use is we should always start by writing clear code that does what is should, and only try to make it faster if we realize that its not fast enough
- profiler: A tool that measures the resources that our code is using, giving us a better undertanding of what's going on 
- cProfile: to analyze a python program, with tool like this we can see how many times is call each frunction and how much time are programs spent on each of them 
- its important write code: easy to undertand, efficiente, maintanible.
- to create a code more faster help to don't use a lot of resources of the computer
- if the code will took you more that 20 mins and you  have option to do it in 10 mins, depending how complex is the task you can selec the option of the code 
- Expensive actions: those that can take a long time to complete
    parsing a file
    reading data over the network
    Iterating through a whole list

## Using the right data structures
- list: are a sequence of elements
- we can remove, add or modify elements in a list
- list disadvantage: use the list to look for just one item can take a lot of time in the case that we work on a huge list. 
java: ArrayList
C++: Vector
Ruby: Array
Go: Slice
- dictionary: store key values pairs
- We add data by associating a value to a key, and we can retrive value looking up a specific key
Java: HashMap
C++: Unordered Map
Ruby: Hash
Go: Map 
- map: mapping between a key and a value
- hash: part comes from the fact that to make the strucure efficient. 
- If you need to access elements by positoin, or will always iterate through all the elements, use a list to sotre them 
- If we need to look up the elements using a key, we'll use a dictionary 

## Expensive loops

- If you do an expensive operation inside a loop, you multiply the time it takes to do the expensive operation by the amount of times you repeat the loop
- for the last case we can optimizce the procees creating a forloop geting all the information in the code
- Make sure that the list of elements that you're iterating through is only as long as you really need it to be. 
- Another thing to rememver about loops is to break out of the loop once you've found what you were looking for. 
- brake: breaking out of loops means that as soon as the data we're looking for if found, our script can continue. 
- When the data is at the beginning of the list and not at the end, it makes sense to have our code break early to make the script faster. 

## Keeping local results
- cache: is a way fo storing data in a form that's faster to access than its original form. 
- the cache can helps us to make more esay the process of store data 
- the cahe don't need to be a huge complex code, some times can be just a varible where you keep the information 
- you can store the information every minute, hour, day, wey... whatever that will be better for you approach
- in the case that we are working with cache, something importat to question us is: 
    What happen if the data is the cache isn't update? 
    When you have to update the cache? 
Q: Your script calculates the average number of active user sessions during business hours in a seven-day period. How often should a local cache be created to give a good enough average withour updating too often? 
R: Once a day 

## Slow script with expensive loop 
- time: mesure speed of commands
    real: the amount of actual time that it took to execute the command
        Wall-clock time
    user: the tiem spent doing operations in the user space
    sys: the siem spend doing system-level operations
- profiler: is a form of dynamic program analysis thath mesures: 
    - the space of time complexity of a program 
    - the use of a particular instruction
    - Frequency and duration of a function calls

syntax: 

```
pprofiler3 -f callgrind -o profiler.out ./<program>
```
pprofiler3: one of the profiles that python can work with 
-f : tell it to use the callfring file format
-o: to tell it to store the ouput in the profile.out

This generate a file that we can open with any tool like: kachegrind

kachegrind: graphical interface for looking into these files


syntax: 
```
kachergrind <filename>
kachergrind profiler.out
```
## Parallelizing operations

- parallel operatinos help us to divide the work in differentes seccions and they can be executing at the same time for example:
    - two or more functions running simulteaneosly 
    - or divide the work in differentes compures
- without the parallel operations that will be happening isthat the script will wait to end the function and then will run the next function 
- concurrency: for the proccess of parallel function exist a root call: concurrency, which work trying to get the more efficient code
- Something very importan is try to undertand which approvhe is better to divide the task 
- Is we have more that one code the OS proces will decide in which will work the task 
- Threads: Let us run parallel tasks inside a process
        modules: Threding or AsyncIO
- A scritp is CPU bound if you are running operations in parallel using all available CPU time
- If we have a lot of task running at the same time, this can cause slowness in our script 

## Slowly growing complexity
- keeping aware we can decide what can you do to keep our system working, like use:

    -data base: to store datas
    - memcached: is a dynamic cacher, can be infront of our Db to make it run faster.
    - caching service like: Varnish, wourld speed up the loead of dynamically created pages
    - loead balancer: destribute the requests
    - cloud: store the data in remote servers 

## Dealing with complex slow system

- Latency is the time it takes for data to pass from one point on a network to another
- to try to understand where is the problem a good question is: where spending the most itme? 
- A company has a single web server hosting a website that also interacts with an external database server. The web server is processing requests very slowly. Checking the web server, you found the disk I/O has high latency. Where is the cause of the slow website requests most likely originating from?  LOCAL DISK
- using index we can have more faster seraching, buuut if we have to many indexex all tables will update and it will be slow
- we need to try to figure out the balance with index for the filedes
- Some time when we have many quieries lock we will need to lock the cache of quires
- and maybe the problem can be case for a lot of request and we maybe will need more servers. 

## Using threads to make things go faster

https://realpython.com/python-concurrency/

- Concurrency: Sequence of instructions that run in oder. 
    *Types: 
    Pre-emptive
    Cooperative 
    Multiprocessing 
- Parallelism: multiple tasks or subtasks of the same task that literally run at the same time

I/O-bound problems: cause your program to slow down because it frequently must wait for input/output (I/O) from some external resource. 

CPU-Bound process: You program spends most of its time doing CPU operations.


### lab
Now, using psutil.disk_io_counters() and psutil.net_io_counters() you'll get byte read and byte write for disk I/O and byte received and byte sent for the network I/O bandwidth. For checking disk I/O, you can use the following command:


>>> import psutil
>>> psutil.cpu_percent()
0.0
>>> psutil.cpu_percent()
0.0
>>> psutil.disk_io_counters()
sdiskio(read_count=6196, write_count=24907, read_bytes=151063040, write_bytes=904693248, read_time=20371, write_time=96464, read_merged_count=0, write_merged_count=22582, busy_time=335664)
>>> psutil.net_io_counters()
snetio(bytes_sent=599590, bytes_recv=147905865, packets_sent=4988, packets_recv=7994, errin=0, errout=0, dropin=0, dropout=0)

### Basics rsync command


# Week 3

## Crashing programs

-  First to try to undertand the problem... look the problem, try to figure out what is happening 
- When you try to undertand the problem, looking the code and making some hypotheses we can reduce the scoop of the problem
- how can we understand the problem?

## System that crash 
- the first thing that we can do to understand arelogs
- We can try to make questions that helps us to reduce the scope
- smart tools: 
    - specific
    - measurable
    - achievable
    - relevant
    - time-based
- the smarts tools can help us to anticipate problems and erros
- we can try to replicate the issue to try to have a better understanding

Q: A user reported an application crashes on their computer. You log in and try to run the program and it crashes again. Which of the following steps would you perform next to reduce the scope of the problem?  REVIEW THE APPLICATIONS LOGS


## Understanding crashing applications
- to have a better undertanding about what is going on with a progam we can look the logs 
    - on linux -> sys log files and Var log 
    - Mac Os -> console app
    - Windows -> viewer
- from the logs of we can have general descriptions, but some times the message will be a little bit cryptic, and in this case we maybe wont have idea about what it dose mean.
- In the case that the logs doesn't work, we can try:
    - search on internet 
    - use another commands that help us to have a better understanding about the program like: 
        - linux strace (system calls)
        - macos dtrusss
        - process monitor windows
 With the additionals tools we can see what is doing the program like: 
    - permision, configuration 
    - logs 
    - infromation about some changes 
- Tring to reproduction case helps us to have a better undertanding abouts what is cuasing the crash 
    - reproduction case as small posible 
- To find the root cause of a crashing application, we'll want to look at all available logs, figure out what, changed, trace the system or library calls the program makes, and create the samallest possible reproduction case. 

## What to do when you can't fix the program? 
- Wrapper: a function or program that provides a compatibility layer between two functions or programs, so they can work well together 
- wrapper: the expected output and input formats don't match 
- If the environment doesn't match we can use: VM or container
- watchdog: a procees that checks whether a program is running and when it's not starts the program again. 
- to create a watchdog we have to write a script and run it in the background, while we run some program 
- Again reproduction case

## Internal server error
- /var/log ---> logs linux
- How can we find which software is listening on port 80? netstat command
- port 80: default web server port 
- netstat command: a lot of informaiton about  network conections depending on the flas we pass
- nginix: popular web serving application out there
- Where is a common location to view configuration files for a web application running on a Linux server?  /etc/<app folder>
- the software is passing the control of the connections to uWSGI which is 
a coomon solution to connect a web server to programs that generate dynamic pages


LOGS LINUX: https://www.fosslinux.com/8984/how-to-check-system-logs-on-linux-complete-usage-guide.htm
LOGS WNS: https://www.digitalmastersmag.com/magazine/tip-of-the-day-how-to-find-crash-logs-on-windows-10/
LOGS MAC: https://www.howtogeek.com/356942/how-to-view-the-system-log-on-a-mac/

COMMAND STRACE: https://www.howtoforge.com/linux-strace-command/

## Accessing Invalid memory
- Invalid memory happen when at the moment when os is maping procees assigned to a protion of the memory, the process is using another portions don't assinged where don't have access or permissions
- the programs like c or c++ work with pointers that this function is assinge where will be assined the memory
- the binarys are created when we convert out program more smaller
- undefined behavior: The code is doing something that's not valid in the programming language. 
- memory valgrind: a very powerful tool that can tell us if the code is doing any invalid operations, no matter if it crashes or not. 
- valgrind: linux and macos
- Dr. Memoty: linux and windows

## Unhandled errors and exceptions

Q: What can you use to notify users when an error occurs, the reason why it occurred, and how to resolve it?  the logging module

## Fixing someone else's code 
- Super important create comments in each program that you create because is someone else use the code... it will be more easy to undertand what is going on vs don't have a head and cola. 
- If you will be start to work with a code that is create for someone else you can started reading the comments or the wikis about it. 
- in the case that you have a new program with 100 lines it can be easy to read the code and try to undertand what is happen ther.
- in the case that you are working with a code with more that 100 lines, a lot of liberys and directorys, meaby can be more easy to read the functions 
- Another intersing thing is that you can use the moduel unittest to created testing for functions, and try to figure out which will be the expected result. 
- After getting acquainted with the program's code, where might you start to fix a problem? Locate the affected function 


## Debugging a segmentation fault
- crach: segmentation fault---> when our applications have a crach like this is useful to have a core file of the crash 
- Core file: Store all the information related to the crash so that we, or someone else, can debug what's going on. Is like to have a screenshot about the how the program runs. 
- but how can we create the core file? 
    
    1: we need to tell to the program that generate the core file, we can use the command ulimit for linux:

        -c: core files
        unlimited: state that we want core files on any size 
        ```
        ~$ ulimit -c unlimited
        ```
    2: run the program again:
 
        ```
        ~$ ulimit -c unlimited
        ~$ ./<program>
        Segmentation fault (core dumped)
        ```   
    3: we have already the core created we can see it: 

        ```
        ~$ ulimit -c unlimited
        ~$ ./<program>
        Segmentation fault (core dumped)
        ~$ ls -l core
        -rw-------- 1 user user 380928Jan 9 14:27 core
        ```
        the file core contains of the information of what was going on with the program when it crashed 
    4: passing it to the gdb debugger we can gdb-c core to give it a core file 

        ```
        gdb -c core exmaple 

            <a lot information like:
                - messages
                - version 
                - licesn
                - etc>

        program termined with signal SIGSEGV, segmentation fault. 
        #0 __strlen_avx2 () at ../sysdeps/x86)64/multiarch/strlen-avz2.S:64
        65 ../sysdeps/x86_64/multiarch/strlen-avx2.S: No such file or directory.
        (gdb)
        ```
    5: to see all the backtrace with the backtrace command 
       up: to move to the calling function in backtrace
       list: line arround the corret one
       print: pirnt values

        ```
        (gdb) backtrace 
        (gdb) up 
        (gdb) list lines
        (gdb) pirnt argv[1]
        ```
 
and this is a way about how we can debuggin in applicaiton that crash in C

Q: When debugging code, what command can you use to figure out how your program reached the faild state? backtrace


## Debuggin a python crash 

- python debugger: pdb3
- the syntax to run pdb3 in put it after the execution of the program and then run it as always

    ```
    pdb3 <namescript> <arguments(if we have)>
    ``
- we can run each of the instructions in the files one by one using the "next" command 
- into the debugger te command "continue" helps us to continue the execution until it either finishes or crashes.
- pirnt for print values
- Byte Order Mark: BOMis used in UTF-16 to tell the difference between a file stored using Little-endian and Big-endian.

# Week 4

## Memory Leaks and how to prevent them 
- Memory leak: a chunk of memory that's no longer needed is not released
-manage memory nenirt cirrectky
- memory leak can afect to programs that are running in the background 
- Lenguges like java an python or Go mange memory for us
- Garbage collector: In charge of freeing the memory that's no longer in use 
- Memory profiler: can help to see how mmush is use it a function 
- Wich of the following descriptions most likely points to a possible memory leak? Application process uses more memory even after a restart. 

## Managing Disk space
- temporaly files
- Which of the following is an example of unnecessary files on a server storage device that can affect applications form running if not cleaned up properly? A set of large tempraty files
- if disk may be getting too full your prcess into what's using the disk? 

## Network saturation 
- the delay bet
- network task factors: latency and bandwidth 
- Latency: Latency is the time it takes for a request to travel from its source to its destination, typically measured in milliseconds (ms). 
- latancy: the amount of time it takes for a request to reach its destination, usually measured in miliseconds(ms)
- Bandwidth: How much data can be sent or received in a second
- Bandwidth avalibe: computers can transmit data to and from many different points of the internet at the same time, each connections will get a poriton of the bandwidth 
- Traffic shaping: A way of marking the data packets sent over the network with different priorities to avoid having huge chunks of data use all of the bandwidth 

## Dealing with memory leaks
- scroll buffer: feature that lets us scroll up and see the things that we executed and their output 
- Decorator: used in python to add extra behavior to functions iwthout having to modify the code
- command top
    RES: dynamic memory that's preserved for the specific process
    SHR: is for memory that's shared across processes 
    VIRT: lists all the virtual memory allocated for each process: process specific memory, shared memory
- It's usually fine for a process to have a high value in the VIRT column. 
- profiler: use profiler help to figure out where our computer's memory is going 
- profiler: memory_profiler to python 
- Decorator: Used in python to add extra behavior to functions without having to modify the code. 
- the profiler give us information about which lines 

https://www.pluralsight.com/blog/tutorials/how-to-profile-memory-usage-in-python

### Note

If you can ping the server but the service isn't available, network connectivity is there and the service is actually down. Many times, you can confirm this with the telnet command. For a Web server that listens on port 80, you simply can issue a command like the following:


telnet www.example.com 80

What you see next will tell you how healthy the server on the other end is.

https://www.linuxjournal.com/content/troubleshooting-network-problems

## Getting to the important tasks
- Eisenhower Decision Matrix: this is a task management tool that help us to organize and prioritize our task. It have two categories:
    urgent
    important
- It's super important try to optimice your time, having important conversion, and have a period of time where you are just working in one task without distracions 
-  we need to make sure that we have the time available to work on tasks that are important, but not necessarily urgent: technical debet. 
- Technical debt: The pending work that accumulates when we choose a quick-and-easy solution instead of applying a sustainable long-term one.

## Prioritizing task 
- Make a list of all the taks that need to get done
- Chech the real ugercy-  something bad can happen?
- Assess the importance of each issue   
    more importan
    important
    not important
- how much enffort they'll take
- If you have a lot of work you can think in two options: 
    - help of members
    - work more hours 
- Its really important try to optimice your time and think which of the task in the list are the most important depending of the way that the system are afecteing. 
- At the same time its important try to figure out how much time each task will be take you to do it, that is another aspecto to consider, in order to create an optimice list of task. 

## Estimating the time task will take 
- it's important be reallystic in the estimate of the time that you will use in the project or task, reallysic not optimistic
- something that we can do to be reallystic is look for another task, compare them and multiplying for 3 or 2 maybe? 
- if you have a huge project, you can divied it in porsions or pices of task, look for the time of each one and then make a sum of time of each one. 

## Communiating expections
- try to be clear and up front about when you expect the issue will be resolved. 
- Ticket tracking system: this help us to see what are doing each of the member of the team.
- Which of the following is an example of a practical shortcut to resolve incidents in a detacenter related to hard drive pre-failures? 
R: Spare drives. 


## Dealing with hard problems
" Everyone knows that debugging is twice as hard as writing a program in the first place. So ir you're as clever as you can be when you write it, how will you ever debug it?"    
- develop code in small, digestible chunks 
- keep your golas clear
- explan the problem to the duck to try to undertand the problem more easly 

## Proactive practices
- If we're the ones writing the code, one thing we can do is to make sure that our code has good unit tests and integration tests. 
- Deploy software in phases of canaries
- Centralized logs collection: A special server that gathers all the logs from all the servers, or even all the computers in the network. 
- If we ask users to provide the needed information up front, we don't have to waste time and go back and forth
- Spent time writting documentation 
 Q: Which proactive practice can you implment to make troubleshooting issues in a program easier when problem arise? R: Inclue debug logging in code. 

## Planning future resource usage
- 
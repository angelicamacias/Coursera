import re 
log = "Jan 31 21:20:33 ubuntu.local ticky: INFO Closed ticket [#3297] (kirknixon)"
err = "Jan 31 21:02:06 ubuntu.local ticky: ERROR Connection to DB failed (breee)"

regex = r"^(.*?) (.*?) (.*?) (.*?) ticky: (INFO|ERROR) (.*?)\[(.*?)\] \((.*?)\)$"
result = re.search(regex, log)
result2= re.search(regex, err)
print(result2.group(6))
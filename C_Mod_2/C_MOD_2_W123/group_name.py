>>> import re
>>> match = re.search('(?P<name>.*) (?P<phone>.*)', 'John 123456')
>>> match.group('name')
'John
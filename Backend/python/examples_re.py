import re

text = "Hi! I am maurya goyal. My number is 124239847238 and #bibds"

match = re.search('maurya',text)
print(match)
print(text[match.start():match.end()])

print(''.join(re.findall(r'\d',text)))
print(''.join(re.findall(r'\D',text)))

print(''.join(re.findall(r'\w+',text)))




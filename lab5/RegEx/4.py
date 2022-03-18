import re

a = input()

pattern = r'(?P<naiti>[A-Z][a-z]+)'

print(re.findall(pattern, a))
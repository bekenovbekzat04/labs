import re

a = input()

pattern = r'[A-Z][a-z]*[0-9]*'

print(re.findall(pattern, a))
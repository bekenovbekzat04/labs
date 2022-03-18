import re
a = input()

pattern = r'\W*\d*[A-Z]*(?P<naiti>[a-z]+_[a-z]+)\W*\d*[A-Z]*'

print(re.search(pattern, a).group('naiti')) if re.search(pattern, a) != None else print('Ne naideno')
import os


mypath = input()
print('Exist:', os.access(mypath, os.F_OK))
print('Readable:', os.access(mypath, os.R_OK))
print('Writable:', os.access(mypath, os.W_OK))
print('Executable:', os.access(mypath, os.X_OK))
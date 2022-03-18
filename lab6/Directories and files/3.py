import os

mypath = input()

print('Existing:', os.path.exists(mypath))

if os.path.exists(mypath):
    print('Filename:', os.path.basename(mypath))
    print('Dirname:', os.path.dirname(mypath))
import os
path = r'C:\Users\User\pp projects\pp2 zhylan'
print("Our directories:", [i for i in os.listdir(path) if os.path.isdir(os.path.join(path, i))])
print("Our files:")
print([i for i in os.listdir(path) if os.path.isfile(os.path.join(path, i))])
print("All directories and files:")
print([i for i in os.listdir(path)])
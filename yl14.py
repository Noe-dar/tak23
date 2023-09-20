import os

path = input("Input path: ")
[root, ext] = os.path.splitext(path)

print(ext[slice(1, len(ext))])
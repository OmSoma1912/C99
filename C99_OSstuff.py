import os
import shutil

path = '/Users/omsoma/Documents/WhiteHatJr/Python_Projects'

root_ext = os.path.splitext(path)

print("root part", root_ext[0])

print("ext part", root_ext[1],"\n")

print("Before moving file:")

print(os.listdir(path))

source = "/Users/omsoma/Documents/WhiteHatJr/Python_Project/C97.py"

destination = "/Users/omsoma/Documents/WhiteHatJr/Python_Project.py"

dest = shutil.move(destination,source)

print("After moving file:")

print(os.listdir(path))



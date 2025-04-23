import os

grits = []

# write a snippet that saves the names of all folders in the current directory to an array
for folder in os.listdir('.'):
    if os.path.isdir(folder):
        grits.append(folder)
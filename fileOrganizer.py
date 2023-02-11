import os
import shutil


path = input("enter the name of the directory to be sorted :- ")


list_of_files = os.listdir(path)

# This will go through each and every file
for file in list_of_files:
    name, ext = os.path.splitext(file)

    # This is going to store the extension type
    ext = ext[1:]

  
    if ext == '':
        continue

    # This will move the file to the directory
    # where the name 'ext' already exists
    if os.path.exists(path+'/'+ext):
       shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

    # This will create a new directory,
    # if the directory does not already exist
    else:
        os.makedirs(path+'/'+ext)
        shutil.move(path+'/'+file, path+'/'+ext+'/'+file)

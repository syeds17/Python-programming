"""Developing a python program to backup a given Folder(Folder in a current working directory) into a ZIP."""

import os
import sys
import pathlib
import zipfile

dirName = input("Enter Directory name that you want to backup : ")  #Input from user

if not os.path.isdir(dirName):
    print("Directory",dirName,"dosen't exists")
    sys.exit(0)

curDirectory = pathlib.Path(dirName)

with zipfile.ZipFile("myZip.zip",mode="w") as archive:   #Converting into a ZipFile.
    for file_path in curDirectory.rglob("*"):
        archive.write(file_path,arcname=file_path.relative_to(curDirectory))
if os.path.isfile("myZip.zip"):           #Printing Result.
    print("Archive","myZip.zip","created successfully")
else:
    print("Error in creating zip archive")            
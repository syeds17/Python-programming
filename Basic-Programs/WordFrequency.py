"""Developing a python program to print 10 most appearing words in a text file."""

import sys
import string  #Importing modules
import os.path

fname = input("Enter the file name : ")    #Taking input text file from user.

if not os.path.isfile(fname):
    print("File",fname,"doesn't exists")
    sys.exit(0)

infile = open(fname,"r")  #Opening file in reading mode.

filecontents = ""

for line in infile:
    for ch in line:
        if ch not in string.punctuation:
            filecontents = filecontents + ch
        else: 
            filecontents = filecontents + ' '     #Replacing punctuations and \n with space

wordFreq = {}
wordList = filecontents.split()

for word in wordList:               #Calculating word Frequency.
    if word in wordFreq.keys():
        wordFreq[word] = 1
    else:
        wordFreq[word] += 1    

sortedWordFreq = sorted(wordFreq.items(),key=lambda x:x[1],reverse=True)  #Sort Dictionary based on values in descending order

print("\n==============================================================") #Displaying 10 most frequently appearing words with their count.
print("10 most frequently appearing words with their count")
print("================================================================")
for i in range (10):
    print(sortedWordFreq[i][0],"occurs",sortedWordFreq[i][1],"times")
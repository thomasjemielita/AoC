# Advent of code Year 2022 Day 7 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import os
from dataclasses import dataclass, field
from typing import List


# Read file # 
fname = os.getcwd()+'/2022/2022/7/'
input_file = open(fname+"input.txt", 'r')
lines = input_file.read().splitlines()
#lines = lines[0:20]

cur_path=[]
folders={}

def pathToString(pathList):
    out=''
    if len(pathList)==1:
        return '/'
    for e in pathList:
        if out=='':
            out=e
        elif out[-1] =='/':
            out+=e
        else:
            out+='/'+e
    return out

## Loop across lines ##
for l in lines:
    if "$ cd .." in l: # Move up a level 
        cur_folder = cur_path.pop()
        str_path = pathToString(cur_path)
    elif "$ cd" in l: # Move to specified space
        cur_folder = l.split()[-1]
        cur_path.append(cur_folder)
        str_path = pathToString(cur_path)
        if str_path not in folders.keys():
            folders[str_path]=0
    elif l.split()[0].isdigit(): # Extract size
        fsize,fname=l.split()
        for i in range(len(cur_path)-1,0,-1):
            parentPath=pathToString(cur_path[:i])
            folders[parentPath]+=int(fsize)
        folders[str_path]+=int(fsize)  


# Part 1: Keep folders with <= 100000
totalSum = 0
for f in folders.keys():
    if folders[f]<=100000:
        totalSum+=folders[f]
print("part1: ",totalSum)

# Part 2: Max space and unused space
MAX_SPACE = 70000000
UNUSED_SPACE = 30000000
freeMem = MAX_SPACE - folders['/']
minSize=freeMem
for f in folders.keys():
    if folders[f]+freeMem>=UNUSED_SPACE:
        if folders[f]<minSize:
            minSize=folders[f]
print("Part2: ", minSize)
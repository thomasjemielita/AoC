# Advent of code Year 2022 Day 9 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import os
import numpy as np

# Read file # 
fname = os.getcwd()+'/2022/9/'
input_file = open(fname+"input.txt", 'r')
lines = input_file.read().splitlines()

# Part 1: Traverse the 2-D #
def coord_update(direct, cur_pos):

    # Initialize #
    new_pos = cur_pos
    x_h, y_h = new_pos[0]

    # Adjust head #
    if direct=="D": 
        y_h -= 1
    if direct=="U": 
        y_h += 1
    if direct=="R": 
        x_h += 1
    if direct=="L": 
        x_h -= 1
    new_pos = list(new_pos)
    new_pos[0] = (x_h, y_h)
    new_pos = tuple(new_pos)

    # Loop through other knots sequentially #
    for ii in range(0, len(new_pos)-1):
        x_h, y_h = new_pos[ii]
        x_t, y_t = new_pos[ii+1]
        
        # Up or Down #
        if direct in ['D', 'U']:
            if direct == 'D': 
                numb_scale = -1
            if direct == "U": 
                numb_scale = 1
            if abs(x_h-x_t)>1 or abs(y_h-y_t)>1:
                y_t = y_t + numb_scale
                if x_h==(x_t-1):
                    x_t = x_t - 1
                if x_h==(x_t+1):
                    x_t = x_t + 1
        # Left or Right 
        if direct in ['L', 'R']:
            if direct == 'L': 
                numb_scale = -1
            if direct == "R": 
                numb_scale = 1
            if abs(x_h-x_t)>1 or abs(y_h-y_t)>1:
                x_t = x_t + numb_scale
                if y_h==(y_t-1): # Diagonal Down
                    y_t = y_t - 1
                if y_h==(y_t+1): # Diagonal Up
                    y_t = y_t + 1
        new_pos = list(new_pos)
        new_pos[ii] = (x_h, y_h)
        new_pos[ii+1] = (x_t, y_t)
        new_pos = tuple(new_pos)
    
    return new_pos

# Loop across lines #
#lines = ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']
## Two Knots (Head/Tail) ##
cur_pos_head = (0, 0)
cur_pos_tail = (0, 0)
cur_pos = (cur_pos_head, cur_pos_tail)
len_path = len(cur_pos)
store_pt1 = []
for line in lines:
    direct, numb = line.split()
    for jj in range(0, int(numb)):
        cur_pos = coord_update(direct, cur_pos)
        if cur_pos[-1] not in store_pt1:
            store_pt1.append(cur_pos[-1])

print("Part One : "+ str(len(store_pt1)))

## 10 Knots: Not the right answer, some type of bug... ##
numb_knots = 10
cur_pos = []
for i in range(0,numb_knots):
    cur_pos.append((0,0))
cur_pos = tuple(cur_pos)
store_pt2 = []
for line in lines:
    direct, numb = line.split()
    for jj in range(0, int(numb)):
        cur_pos = coord_update(direct, cur_pos)
        if cur_pos[-1] not in store_pt2:
            store_pt2.append(cur_pos[-1])

print("Part Two : "+ str(len(store_pt2)))



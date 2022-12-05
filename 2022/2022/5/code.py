# Advent of code Year 2022 Day 5 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import time
import numpy as np
import pandas as pd

# Read file # 
input_file = open("input.txt", 'r')
input = input_file.read().split('\nmove')

# Set up the base stack (parse?) #
# base_mat = input[0].split('\n')
# numb_cols = base_mat[-2].split(' ')
# for item in numb_cols.copy():
#   if item=='':
#     numb_cols.remove(item)
# numb_array = [int(numeric_string) for numeric_string in numb_cols]
# max_cols = max(numb_array)

# Set up base time: manually to be faster #
stacks_org = [0, # Add zero to avoid using i-1 on re-stacking (easier?)
list('QGPRLCTF'),
list('JSFRWHQN'),
list('QMPWHBF'),
list('FDTSV'),
list('ZFVWDLQ'),
list('SLCZ'),
list('FDVMBZ'),
list('BJT'),
list('HPSLGBNQ')]

# Set up moves data #
input_moves = input.copy()
input_moves.remove(input[0])
moves = []
for line in input_moves:
    line = line.split()
    moves.append( (int(line[0]), int(line[2]), int(line[4])) )
    
# Part 1: Loop through moves and re-stack cargo #
stacks_p1 = stacks_org.copy()
for n, i, j in moves:
  chunk = stacks_p1[i][:n][::-1]
  stacks_p1[i] = stacks_p1[i][n:]
  stacks_p1[j] = chunk + stacks_p1[j]

part1_string = ''.join([stack_col[0] for stack_col in stacks_p1[1:]])

print('Part 1 string:' + part1_string)
  
# Part 2: When moving from stack i to j, the order is retained
stacks_p2 = stacks_org.copy()
for n, i, j in moves:
  chunk = stacks_p2[i][:n]
  stacks_p2[i] = stacks_p2[i][n:]
  stacks_p2[j] = chunk + stacks_p2[j]

part2_string = ''.join([stack_col[0] for stack_col in stacks_p2[1:]])

print('Part 2 string:' + part2_string)

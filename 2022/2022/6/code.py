# Advent of code Year 2022 Day 6 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import time
import sys
import numpy as np
import pandas as pd

# Read file # 
input_file = open("input.txt", 'r')
input = input_file.read()
#input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb" # Should be 7

# Functions #
def find_marker(input_array, numb):
  
  if len(input_array) < 4:
    print("Must contain at least 4 signals")
    sys.exit()
    
  marker = 0
  for i in range(numb, len(input_array)+1, 1):
    sub = input_array[(0+i-numb):(i)]
    if len(np.unique(sub))==numb: 
      marker = i
      break
    
  return marker
  
#### Part I ####
print("Starting Part One")
start_time = time.time()
input_list = [*input]
input_array = np.array(input_list)

part1_mark = find_marker(input_array = input_array, numb=4)
  
part_one_time = time.time() - start_time
print("Part One ({time} s): {value}".format(time = round(part_one_time,3), value = str(part1_mark)))
  
#### Part II ####
print("Starting Part One")
start_time = time.time()
input_list = [*input]
input_array = np.array(input_list)

part2_mark = find_marker(input_array = input_array, numb=14)
  
part_two_time = time.time() - start_time
print("Part Two ({time} s): {value}".format(time = round(part_two_time,3), value = str(part2_mark)))

# Advent of code Year 2022 Day 10 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import os
import numpy as np

# Read file # 
fname = os.getcwd()+'/2022/2022/10/'
input_file = open(fname+"input.txt", 'r')
lines = input_file.read().splitlines()


### Part 1 ####
def parse_instr_store(cycle, cur_val, cycles_sel, store):
    
    if cycle in cycles_sel:
        store_pt1.append(cycle*cur_val)
    cycle += 1
    return cycle, store

# Initialize Part 1#
cycles_sel = [20,60,100,140,180,220]
cycle = 1
cur_val = 1
store_pt1 = []
val = 0
for ll in lines:
    # Initialize #
    init = ll.split(' ')
    instr = init[0]

    # Parse and check if we need to store strength #
    cycle, store_pt1 = parse_instr_store(cycle, cur_val, cycles_pt1, store_pt1) 

    # ADDX #
    if instr=="addx": 
        #print("addx")
        addx_numb = int(init[1])
        cycle, store_pt1 = parse_instr_store(cycle, cur_val, cycles_sel, store_pt1) 
        cur_val += addx_numb

### Part 2 ###

########### PART TWO ##################
# From Trent Huhn #
print("Starting Part Two")

def evaluate_cycle_pt2(cycle,x_val,output):
    pixel = '.'   
    if len(output) <= (cycle - 1) // HORZ_PIXELS: output.append([]) # use integer division to check if we have to add a new row to our output array
    if (cycle - 1) % HORZ_PIXELS in [x_val-1,x_val,x_val+1]: # use modulo to determine current horizontal position based on cycle #
        pixel = '#'
    output[(cycle - 1) // HORZ_PIXELS].append(pixel)
    cycle += 1
    return cycle,output

x_val = 1
cycle = 1
HORZ_PIXELS = 40
output = []
val = 0
for i,line in enumerate(input):
    line = line.split(' ')
    inst = line[0]
    if len(line) > 1: val = int(line[1])

    # increment cycle and update output array based on current sprite position
    cycle,output = evaluate_cycle_pt2(cycle,x_val,output) 

    if inst == "addx":
        cycle,output = evaluate_cycle_pt2(cycle,x_val,output) 
        x_val += val # finally, finish the addx instruction

# Print the output to the screen
for i in range (0,len(output)):
    print(''.join(output[i]))


part_two_time = time.time() - start_time
print("Part Two ({time} s): {value}".format(time = round(part_two_time,3), value = str(None)))


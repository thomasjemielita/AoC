# Advent of code Year 2022 Day 11 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import os
import re
from math import prod

# Read file # 
fname = os.getcwd()+'/2022/2022/11/'
input_file = open(fname+"input.txt", 'r')
lines = input_file.read().split('\n\n')

# Functions #

def monkey_dict(input):
    dict = {}
    pieces = input.split('\n')
    dict['number'] = int(re.findall(r'\d+', pieces[0])[0])
    items_list = re.findall(r'\d+', pieces[1])
    dict['items'] = [int(i) for i in items_list]
    dict['operation'] = pieces[2]
    dict['test'] = int(re.findall(r'\d+', pieces[3])[0])
    dict['true'] = int(re.findall(r'\d+', pieces[4])[0])
    dict['false'] = int(re.findall(r'\d+', pieces[5])[0])
    dict['inspect_number'] = 0

    return dict

def parse_operation(operator, cur_val, round_down=3, adjuster=0):
    new_val = 0
    # Perform Operation #
    parts = operator.split()
    var1 = parts[3]
    var2 = parts[5]
    if (var1=='old'):
        var1 = cur_val
    if (var2=='old'):
        var2 = cur_val
    else: var2 = int(var2)
    if (parts[4]=="+"):
        new_val = var1 + var2
    if (parts[4]=="-"):
        new_val = var1 - var2
    if (parts[4]=="*"):
        new_val = var1 * var2
    if (parts[4]=="/"):
        new_val = var1 / var2
    # Divide by number and round down #
    new_val = new_val // round_down
    if adjuster!=0:
        new_val = new_val % adjuster
    return new_val

def update_monkey_pt1(index, Dict, round_down=3, adjuster=0):

    monkey = Dict[index]

    # Check if there are items #
    if len(monkey['items'])==0:
        return Dict

    # Otherwise, loop through items and update value
    new_items = []
    for item in monkey['items']:
        new_items.append(parse_operation(operator=monkey['operation'], cur_val=item, round_down=round_down, adjuster=adjuster))
        Dict[index]['inspect_number'] += 1
    #print(new_items)
    #divisible_list = [x % monkey['test'] for x in new_items]

    for i, itemz in enumerate(new_items):
        if (itemz % monkey['test'])==0:
            throw_to = monkey['true']
        else:
            throw_to = monkey['false']
        Dict[throw_to]['items'].append(itemz)

    Dict[index]['items'] = []

    return Dict

## Part 1: Find Top Two Monkeys ##
DictMonkey = {}
for i, monkey in enumerate(lines):
    DictMonkey[i] = monkey_dict(input=monkey)
 
ROUNDS = 20
round_numb= 3
for r in range(0, ROUNDS, 1):
    #print("Round" + str(r))
    for ii in DictMonkey:
        #print("Monkey" + str(ii))
        DictMonkey = update_monkey_pt1(index=ii, Dict=DictMonkey, round_down=round_numb)

inspect_numbers = []
for ii in DictMonkey:
    inspect_numbers.append(DictMonkey[ii]['inspect_number'])
inspect_numbers.sort()
part1_ans = inspect_numbers[-1]*inspect_numbers[-2]

print("Part One : "+ str(part1_ans))

#### Part Two: No rounding down, 10000 rounds ###

DictMonkey_pt2 = {}
for i, monkey in enumerate(lines):
    DictMonkey_pt2[i] = monkey_dict(input=monkey)

# Math Trick: After "rounding" (if used, we divide by product of all divisibles)
monkey_divis = []
for monk in DictMonkey_pt2:
    monkey_divis.append(DictMonkey_pt2[monk]['test'])
prod_divis = prod(monkey_divis)

ROUNDS = 10000
round_numb = 1
for r in range(0, ROUNDS, 1):
    print("Round" + str(r))
    for ii in DictMonkey_pt2:
        #print("Monkey" + str(ii))
        DictMonkey_pt2 = update_monkey_pt1(index=ii, Dict=DictMonkey_pt2, round_down=1, adjuster=prod_divis)

inspect_numbers = []
for ii in DictMonkey_pt2:
    inspect_numbers.append(DictMonkey_pt2[ii]['inspect_number'])
inspect_numbers.sort()
part2_ans = inspect_numbers[-1]*inspect_numbers[-2]

print("Part Two : "+ str(part2_ans))
# Advent of code Year 2022 Day 8 solution
# Author = Thomas Jemielita
# Date = December 2022

# Modules #
import os
import numpy as np

# Read file # 
fname = os.getcwd()+'/2022/2022/8/'
input_file = open(fname+"input.txt", 'r')
lines = input_file.read().splitlines()

# Part One + Part Two #

# Create stacked array #
list_mat = []
for l in lines:
    list_mat.append([*l])
array = np.array(list_mat)

n_row, n_col = array.shape

# Search above, below, right, left #
def location_checker(array, i, j):

    val = array[i][j]

    # Search above #
    above_check = np.sum(array[:,j][0:i] < val)
    above_len = len(array[:,j][0:i])
    above_cnt = 0 
    for ii in range(i-1, -1, -1): 
        above_cnt += 1
        if ii==0 or array[:,j][ii] >= val: break

    # Search below #
    below_check = np.sum(array[:,j][(i+1):] <  val)
    below_len = len(array[:,j][(i+1):])
    below_cnt = 0
    for ii in range(i+1, n_row, 1):
        below_cnt += 1
        if ii==(n_row-1) or array[:,j][ii] >= val: break

    # Search right #
    right_check = np.sum(array[i][(j+1):] <  val)
    right_len = len(array[i][(j+1):])
    right_cnt = 0
    for jj in range(j+1, n_col, 1):
        right_cnt += 1
        if jj==(n_col-1) or array[i][jj] >= val: break

    # Search Left #
    left_check = np.sum(array[i][0:j] <  val)
    left_len = len(array[i][0:j])
    left_cnt = 0
    for jj in range(j-1, -1, -1):
        left_cnt += 1
        if jj==0 or array[i][jj] >= val: break
    
    # Check if visible #
    if (above_check==above_len) or (below_check==below_len) \
        or (right_check==right_len) or (left_check==left_len):
        see_any = 1
    else: see_any = 0
    # Visibility Score #
    vis_score = left_cnt*right_cnt*below_cnt*above_cnt

    return {'see_any': see_any, 'vis_score': vis_score, 'above':above_cnt, 'below': below_cnt, 'left': left_cnt, 'right': right_cnt}

        

## Loop through forest ##
forest = []
forest_vals = []
for i in range(0, n_row, 1):
    for j in range(0, n_col, 1):
        if (i in (0, n_row-1)) or (j in (0, n_col-1)):
            forest.append(1)
        else:
            val = array[i][j]
            ind_ij = location_checker(array, i, j)
            forest_vals.append(ind_ij['vis_score'])
            if ind_ij['see_any']==1: forest.append(1)

print("Part One : "+ str(len(forest)))
print("Part Two : "+ str(max(forest_vals)))

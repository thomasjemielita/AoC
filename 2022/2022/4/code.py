# Advent of code Year 2022 Day 4 solution
# Author = Thomas Jemielita
# Date = December 2022

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    
# Start timer #
print("Starting Timer)
start_time = time.time()

# Set up data (avoid loop by using pandas) #
df = pd.DataFrame(input, columns = ['pairs'])
df['elf1'] = df['pairs'].str.split(',').str[0]
df['elf2'] = df['pairs'].str.split(',').str[1]
df['elf1_min'] = df['elf1'].str.split('-').str[0]
df['elf1_max'] = df['elf1'].str.split('-').str[1]
df['elf2_min'] = df['elf2'].str.split('-').str[0]
df['elf2_max'] = df['elf2'].str.split('-').str[1]
elf_vals = ['elf1_min', 'elf1_max', 'elf2_min', 'elf2_max']
df[elf_vals] = df[elf_vals].apply(pd.to_numeric)

# Check if elfs overlap (1 within 2, and 2 within 1) #
df['check_1_2'] = (df['elf2_min'] <= df['elf1_min']) & (df['elf1_min'] <= df['elf2_max']) \
                   & (df['elf2_min'] <= df['elf1_max'] )& (df['elf1_max'] <= df['elf2_max']) 
                   
df['check_2_1'] = (df['elf1_min'] <= df['elf2_min']) & (df['elf2_min'] <= df['elf1_max']) \
                   & (df['elf1_min'] <= df['elf2_max'] )& (df['elf2_max'] <= df['elf1_max']) 

# Select instances where one or both elfs overlap #
num_overlapping_pairs = df.loc[df['check_1_2'] | df['check_2_1']].shape[0]

stop_time = time.time() - start_time
print("Total ({time} s): {value}".format(time = round(stop_time,3), value = str(num_overlapping_pairs)))

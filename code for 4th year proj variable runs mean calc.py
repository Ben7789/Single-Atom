# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 10:58:50 2025

@author: rolan
"""


import matplotlib.pyplot as plt
import numpy as np
import random
import math

def create_vertical_dimer_grid(grid_sizex, grid_sizey):
   
    # Ensure the grid has an even number of rows for full vertical dimers
    if grid_sizey % 2 != 0:
        raise ValueError("Grid height (grid_sizey) must be even for proper vertical dimers.")

    # Initialize empty grid
    darray = np.zeros((grid_sizey, grid_sizex), dtype=int)
    
    # Fill the grid with vertical dimers
    for x in range(grid_sizex):  
        for y in range(0, grid_sizey, 2):  # Step by 2 to place dimers
            darray[y, x] = 3   # Top part of the dimer
            darray[y+1, x] = 4 # Bottom part of the dimer

    return darray

# Example Usage
grid_sizex = 40
grid_sizey = 40
dimer_grid = create_vertical_dimer_grid(grid_sizex, grid_sizey)

def get_next_step(darray, initial_step):
    x, y = initial_step
    
    # Define movement directions with wrap-around behavior
    up = (x - 1, y) if x > 0 else (darray.shape[0] - 1, y)
    down = (x + 1, y) if x < darray.shape[0] - 1 else (0, y)
    left = (x, y - 1) if y > 0 else (x, darray.shape[1] - 1)
    right = (x, y + 1) if y < darray.shape[1] - 1 else (x, 0)
    
    # Determine movement based on the current cell value
    if darray[initial_step] == 1:
        if darray[right] == 2:
            return right
    
    if darray[initial_step] == 2:
        if darray[left] == 1:
            return left

    if darray[initial_step] == 3:
        if darray[down] == 4:
            return down

    if darray[initial_step] == 4:
        if darray[up] == 3:
            return up

    return initial_step  # If no valid move, stay in place

def get_neighbours(darray, next_step):
    x, y = next_step
    if darray[next_step] == 1:
        direction = ["left", "up", "down"]
    
    if darray[next_step] == 2:
        direction = ["right", "up", "down"]
    
    if darray[next_step] == 3:
        direction = ["up", "left", "right"]
    
    if darray[next_step] == 4:
        direction = ["down", "left", "right"]
        
    directionchoice = random.choice(direction)
    
    if directionchoice == "up":
        neighbour = (x - 1, y) if x > 0 else (darray.shape[0] - 1, y)
        darray[next_step] = 4
        
    if directionchoice == "down":
        neighbour = (x + 1, y) if x < darray.shape[0] - 1 else (0, y)
        darray[next_step] = 3
    
    if directionchoice == "left":
        neighbour = (x, y - 1) if y > 0 else (x, darray.shape[1] - 1)
        darray[next_step] = 2
        
    if directionchoice == "right":
        neighbour = (x, y + 1) if y < darray.shape[1] - 1 else (x, 0)
        darray[next_step] = 1
    return directionchoice, neighbour

#def meancalc()

"""   
def get_neighbours(darray, next_step):
    x, y = next_step
    if darray[next_step] == 1:
        neighbours = [(x, y - 1) if y > 0 else (x, darray.shape[1] - 1),
                      (x - 1, y) if x > 0 else (darray.shape[0] - 1, y),
                      (x + 1, y) if x < darray.shape[0] - 1 else (0, y)]
    
    if darray[next_step] == 2:
        neighbours = [(x, y + 1) if y < darray.shape[1] - 1 else (x, 0),
                      (x - 1, y) if x > 0 else (darray.shape[0] - 1, y),
                      (x + 1, y) if x < darray.shape[0] - 1 else (0, y)]
    
    if darray[next_step] == 3:
        neighbours = [(x - 1, y) if x > 0 else (darray.shape[0] - 1, y),
                      (x, y - 1) if y > 0 else (x, darray.shape[1] - 1),
                      (x, y + 1) if y < darray.shape[1] - 1 else (x, 0)]
    
    if darray[next_step] == 4:
        neighbours = [(x + 1, y) if x < darray.shape[0] - 1 else (0, y),
                      (x, y - 1) if y > 0 else (x, darray.shape[1] - 1),
                      (x, y + 1) if y < darray.shape[1] - 1 else (x, 0)]
    neighbourschoice = random.choice(neighbours)
    return neighbourschoice
"""        
        
                      
# Example Usage
grid_sizex = 40
grid_sizey = 40
darray = create_vertical_dimer_grid(grid_sizex, grid_sizey)
vdimercount = np.array(np.count_nonzero(darray == 3))
path = np.array([])
"""
Key:
    0 : empty
    1 : left
    2 : right
    3 : up
    4 : down
"""

runs = 1000
vdimercount = np.zeros(runs+1)
vdimercount[0] = np.count_nonzero(darray == 3)
for i in range(1, runs + 1):
    random_index = tuple(np.random.randint(dim) for dim in darray.shape)
    path = np.append(path, random_index)
    next_step = get_next_step(darray, random_index)
    while next_step != random_index:
        path = np.append(path, next_step)
        
        directionchoice, neighbour = get_neighbours(darray, next_step)
        
        darray[random_index]= 0
        
        next_step = get_next_step(darray, neighbour)
        if directionchoice == "up":
            darray[neighbour] = 3
        if directionchoice == "down":
            darray[neighbour] = 4
        if directionchoice == "left":
            darray[neighbour] = 1
        if directionchoice == "right":
            darray[neighbour] = 2
    vdimercount[i] = np.count_nonzero(darray == 3)



plt.figure(figsize=(8, 5))  # Set figure size
plt.plot(range(runs+1), vdimercount, linestyle='-', color='b', linewidth=3, markersize=6, label="Dimer Count")

# Set y-axis range from max value to 0
plt.ylim(0, max(vdimercount) )

# Labels and title
plt.xlabel("Runs", fontsize=12)
plt.ylabel("Vertical Dimer Count", fontsize=12)
plt.title("Vertical Dimer Count Over Runs", fontsize=14)

# Add grid for readability
plt.grid(True, linestyle='--', alpha=0.6)

# Show legend
plt.legend()

# Show the plot
plt.show()

meanarray = vdimercount[75:]

#Find the length of the array
length = len(meanarray)

split = 9
# If not divisible by split, remove extra elements from the end
if length % split != 0:
    new_length = length - (length % split)  # Make it divisible by split
    meanarray = meanarray[:new_length]  # Trim the array

sub_arrays = np.split(meanarray, split)
std_arrays = np.zeros(split)
se = np.zeros(split)
meansplit = np.zeros(split)
for a in range(split):
    std_arrays[a] = np.std(sub_arrays[a])
    se[a] = std_arrays[a]/np.sqrt(new_length/split)
    meansplit[a] = np.mean(sub_arrays[a])
    
final_mean = np.mean(meansplit)
standard_error = np.sum(std_arrays)/np.sqrt(new_length)
for a in range(len(meansplit)):
    print(f"Mean: {meansplit[a]}, Std: {std_arrays[a]}")
    
print(f"The final mean: {final_mean}, standard error: {standard_error}")

    







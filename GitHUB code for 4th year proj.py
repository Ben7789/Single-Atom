# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 10:36:12 2025

@author: rolan
"""

import matplotlib.pyplot as plt
import numpy as np
import random

grid_size = 4
x, y = np.meshgrid(range(grid_size), range(grid_size))
plt.figure(figsize=(6, 6))
plt.scatter(x, y, color="black", s=30)

def worm_algorithm(dimers, grid_size):
    (x_start, y_start) = (random.randint(0, grid_size - 1), random.randint(0, grid_size - 1))
    for i, dimer in enumerate(dimers):
        if (x_start, y_start) in dimer:
            (x1, y1), (x2, y2) = dimer
            break
    else:
        return dimers 
    
    # Remove the selected dimer
    dimers.remove([(x1, y1), (x2, y2)])
    plt.plot(x1, y1, 'bo' )
    plt.plot(x2, y2, 'mo')
#    plt.plot([x1, x2], [y1, y2], color="green", linewidth=3)
    
    # Choose a new neighbor to move to
    dimer.remove((x_start, y_start))

    neighbours = [(dimer[0][0] + 1, dimer[0][1]), (dimer[0][0], dimer[0][1] + 1), (dimer[0][0], dimer[0][1] - 1), (dimer[0][0] - 1, dimer[0][1])]
    neighbourscorrect = []
    neighbours.remove((x_start, y_start))
    for x, y in neighbours:
        if x < 0:
            x = grid_size-1
        elif x > grid_size-1:
            x = 0
        elif y < 0:
            y = grid_size-1
        elif y > grid_size-1:
            y = 0
        neighbourscorrect.append((x,y))
        
        
    new_pos = random.choice(neighbourscorrect)
    

    dimers.append([(dimer[0][0], dimer[0][1]), new_pos])
 
    while (new_pos) != (x_start, y_start):
        for i, dimer in enumerate(dimers):
            if (new_pos) in dimer:
                (x1, y1), (x2, y2) = dimer
                break
        else:
            return dimers 
        
        dimers.remove([(x1, y1), (x2, y2)])
        dimer.remove((new_pos[0], new_pos[1]))
        
        neighbours = [(dimer[0][0] + 1, dimer[0][1]), (dimer[0][0], dimer[0][1] + 1), (dimer[0][0], dimer[0][1] - 1), (dimer[0][0] - 1, dimer[0][1])]
        neighbourscorrect = []
#        neighbours.remove((new_pos[0], new_pos[1]))
        for x, y in neighbours:
            if x < 0:
                x = grid_size -1
            elif x > grid_size -1:
                x = 0
            elif y < 0:
                y = grid_size -1
            elif y > grid_size -1:
                y = 0
            neighbourscorrect.append((x,y))
        neighbourscorrect.remove((new_pos[0], new_pos[1]))
        new_pos = random.choice(neighbourscorrect)
        dimers.append([(dimer[0][0], dimer[0][1]), new_pos])


            
            
    return dimers


dimers = [
    [(0, 0), (1, 0)],
    [(2, 0), (3, 0)],
    [(0, 1), (0, 2)],
    [(1, 1), (2, 1)],
    [(0, 3), (1, 3)],
    [(2, 3), (3, 3)],
    [(1, 2), (2, 2)],
    [(3, 1), (3, 2)]
]


dimers = worm_algorithm(dimers, grid_size)
for dimer in dimers:
    (x1, y1), (x2, y2) = dimer
    if x1 == 0 and x2 == grid_size - 1:
        plt.plot([x1, -1], [y1, y2], color="red", linewidth=3)
        plt.plot([grid_size , x2], [y1, y2], color="red", linewidth=3)
    elif x1 == grid_size - 1 and x2 == 0:
        plt.plot([x2, -1], [y2, y1], color="red", linewidth=3)
        plt.plot([grid_size , x1], [y2, y1], color="red", linewidth=3)
    elif y1 == 0 and y2 == grid_size - 1:
         plt.plot([x1, x2], [y1, -1], color="red", linewidth=3)
         plt.plot([x1, x2], [grid_size, y2], color="red", linewidth=3)
    elif y1 ==  grid_size - 1 and y2 == 0:
         plt.plot([x2, x1], [y2, -1], color="red", linewidth=3)
         plt.plot([x2, x1], [grid_size, y1], color="red", linewidth=3)
    else:
        plt.plot([x1, x2], [y1, y2], color="red", linewidth=3)





plt.xlim(-0.5, grid_size - 0.5)
plt.ylim(-0.5, grid_size - 0.5)
plt.gca().set_aspect('equal', adjustable='box')
plt.axis('off')
plt.show()

import numpy as np

serial = 1309
grid_size = 300

def power_level(x,y):
    ID = x + 10
    power = ID*y
    power += serial
    power *= ID
    power = ((power%1000)-(power%100))//100
    power -= 5
    return power

def partial_sums():
    #Fills  grid with the partial sums
    grid = np.zeros((grid_size+1, grid_size+1))
    for i in range(1,grid_size+1):
        for j in range(1,grid_size+1):
            grid[i,j] = grid[i-1,j] + grid[i,j-1] + power_level(i,j) - grid[i-1,j-1]
    return grid

def find_sum(grid,i,j,size):
    return grid[i+size-1,j+size-1] - grid[i-1,j+size-1] - grid[i+size-1,j-1] + grid[i-1,j-1]

def largest_sum(grid, size):
    #Input: grid of partial sums, size of window
    best_pos = (1,1)
    best_pow = -10*grid_size**2
    for i in range(1,grid_size + 1 - size):
        for j in range(1,grid_size+1-size):
            power = find_sum(grid,i,j,size)
            if power > best_pow:
                best_pow = power
                best_pos= (i,j)
    return (best_pos,best_pow)

def largest(grid):
    best_pos=(1,1)
    best_pow=0
    best_size=0
    for size in range(1,grid_size+1):
        (pos, power) = largest_sum(grid,size)
        #print(size, pos, power)
        if power > best_pow:
            best_pos=pos
            best_pow=power
            best_size = size
    return (best_pos,best_size, best_pow)

grid = partial_sums()
#print(find_sum(grid,33,45,3))
#print(largest_sum(grid,27))
print(largest(grid))


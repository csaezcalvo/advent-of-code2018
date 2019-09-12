import numpy as np

serial = serial = 1309

def power_level(x,y):
    ID = x + 10
    power = ID*y
    power += serial
    power *= ID
    power = ((power%1000)-(power%100))//100
    power -= 5
    return power


def fill_grid():
    for i in range(1,301):
        for j in range(1,301):
            grid[i,j] = power_level(i,j)
    return grid

def largest_sum(grid, size):
    best = (1,1)
    best_pow = 0
    for i in range(1,300-size):
        for j in range(1,300-size):
            power = sum(sum(grid[i:i+size,j:j+size]))
            if power > best_pow:
                best_pow = power
                best = (i,j)
    return (best, best_pow)

grid = np.zeros((301,301))
grid = fill_grid()
print(largest_sum(grid,3))

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

def find_sum(x,y,size):
    total = 0
    for i in range(size):
        for j in range(size):
            total += power_level(x+i,y+j)
    return total

def find_largest(size):
    best = (1,1)
    best_pow = find_sum(1,1,size)
    for i in range(1,grid_size-size+1):
        for j in range(1,grid_size-size+1):
            power = find_sum(i,j,size)
            if power > best_pow:
                best_pow = power
                best = (i,j)
    return (best, best_pow)


def find_largest_absolute():
    best_size = 300
    (best_pos, best_power) = find_largest(1)
    for i in range(1,300):
        (pos,power) = find_largest(i)
        if power > best_power:
            best_size=i
            best_power = power
            best_pos = pos
        print(i, best_power,best_pos)
    return (best_pos,best_size,best_power)
            
        
                
    

print(find_largest_absolute())

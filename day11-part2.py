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

file_path="/home/carlos/advcode2018/input13"
file = open(file_path,'r')

test_data = ['/>-<\\  ','|   |  ','| /<+-\\','| | | v','\\>+</ |','  |   ^','  \\<->/']
test_data2 = ['/->-\\        ','|   |  /----\\','| /-+--+-\\  |','| | |  | v  |',
              '\\-+-/  \\-+--/','  \\------/   ']
test_data3 = ['------><-----']
 

data = []
carts_pos = []
i=0
#for line in test_data:
for line in file:
    row =[]
    j=0
    for x in line:
        if x == '^':
            row.append('|')
            carts_pos.append([0,[i,j],0])
        elif x == '>':
            row.append('-')
            carts_pos.append([1,[i,j],0])            
        elif x == 'v':
            row.append('|')
            carts_pos.append([2,[i,j],0])
        elif x == '<':    
            row.append('-')
            carts_pos.append([3,[i,j],0])
        elif x != '\n':
            row.append(x)
        j += 1
    i += 1
    data.append([x for x in row if x != '\n'])

def sort(carts_pos):
    pos = [[cart[1][1],cart[1][0]] for cart in carts_pos]
    indices = sorted(range(len(pos)), key=lambda k: pos[k])
    new_carts = []
    for i in indices:
        new_carts.append(carts_pos[i])
    return new_carts

    
def move_collide(data,carts_pos):
    #print(carts_pos)
    carts_pos=sort(carts_pos)
    new_pos=carts_pos.copy()
    for cart in carts_pos:
        #Move a cart
        if cart[0] == 0:
            cart[1][0] -= 1
        elif cart[0] == 1:
            cart[1][1] += 1
        elif cart[0] == 2:
            cart[1][0] += 1
        elif cart[0] == 3:
            cart[1][1] -= 1

        #Check collisions after move and remove colliding carts
        rep = check_collision(new_pos) 
        if rep:
            new_pos = [cart for cart in new_pos if not(cart[1] in rep)]

        #Take care of intersections and changes of direction
        if data[cart[1][0]][cart[1][1]] == '+':
            cart[0] = (cart[0] + cart[2]-1)%4
            cart[2] = (cart[2]+1)%3
        elif data[cart[1][0]][cart[1][1]] == '/':
            if cart[0] == 0:
                cart[0] = 1
            elif cart[0] == 1:
                cart[0] = 0
            elif cart[0] == 2:
                cart[0] = 3
            elif cart[0] == 3:
                cart[0] = 2
        elif data[cart[1][0]][cart[1][1]] == '\\':
            if cart[0] == 0:
                cart[0] = 3
            elif cart[0] == 1:
                cart[0] = 2
            elif cart[0] == 2:
                cart[0] = 1
            elif cart[0] == 3:
                cart[0] = 0
    return new_pos

def check_collision(carts_pos):
    pos = [cart[1] for cart in carts_pos]
    repeated = []
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i != j and pos[i] == pos[j]:
                repeated.append(carts_pos[j][1])
    return repeated

def iter(data,carts_pos):
    tick = 0
    while check_collision(carts_pos) == False:
        print(tick)
        carts_pos = move(data,carts_pos)
        tick +=1
    return check_collision(carts_pos)

def last_survivor(data, carts_pos):
    tick = 0
    while len(carts_pos) > 1:
        #if tick >-1:
        #    show_data(data,carts_pos)
        if tick%100 == 0:
            print(tick, len(carts_pos))
        carts_pos = move_collide(data,carts_pos)
        tick +=1
    show_data(data,carts_pos)
    return (tick, carts_pos)

    
def show_data(data, carts_pos):
    d = { 0:'^',1:'>',2:'v',3:'<'}
    new_data = []
    for x in data:
        y = x.copy()
        new_data.append(y)
    for cart in carts_pos:
        new_data[cart[1][0]][cart[1][1]] = d[cart[0]]
    for row in new_data:
        print(''.join(row))
    #print(data)
    
#print(carts_pos)
#print(sort(carts_pos))

print(last_survivor(data,carts_pos))

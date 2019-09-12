file_path = "/home/carlos/advcode2018/input15"
file=open(file_path,'r')
data = []
players= []
i=0
for line in file:
    j=0
    row = []
    for x in line:
        if not(x in ['G','E','\n']):
           row.append(x)
        elif x == 'G':
            players.append(['G',[i,j], 200])
            row.append('.')
        elif x == 'E':
            players.append(['E',[i,j], 200])
            row.append('.')
        j +=1
    data.append(row)
    i += 1

def show_data(data, players):
    new_data = data.copy()
    for player in players:
        new_data[player[1][0]][player[1][1]] = player[0]
    for row in new_data:
        print(''.join(row))

def sort(players):
    pos = [player[1] for player in players]
    indices = sorted(range(len(pos)), key=lambda k: pos[k])
    new_players = []
    for i in indices:
        new_players.append(players[i])
    return new_players

def man_dist(x,y):
    return abs(x[0]-y[0]) + abs(x[1] - y[1])


### REVISE TO MAKE IT THE SHORTEST PATH
def shortest_path(data, players, pos1,pos2):
    #Returns the first step in order of a shortest path from pos1 to pos2
    path = [pos1]
    dead = []
    current = pos1
    while current != pos2 and not(pos1 in dead):
        reachable = [[x,y] for x in range(current[0]-1,current[0]+2)
                 for y in range(current[1]-1,current[1]+2) if (man_dist(current, [x,y]) == 1 and data[x][y] == '.'
                                                               and not([x,y] in dead))]
        if len(reachable) == 0:
            current = path[-1]
            x = path.pop()
            dead.append(x)
            continue
        nearest = min(reachable, key = lambda k: man_dist(k,pos2))
        current = nearest
        path.append(current)
    if pos1 in dead:
        return False
    else:
        return path

print(shortest_path(data, players, [12,11], [12,20]))
    

def move(data, players, player):
    pass

def attack(data, player, enemy):
    enemy[2]-= 3
    

def turn(data, players, player):
    players = sort(players) #Sort the players by position
    
    if player[0] == 'G':
        enemies = [x for x in players if x[0] == 'E']
    else:
        enemies = [x for x in players if x[0] == 'G']
    #Checks if there are enemies
    if enemies == []:
        return False #Maybe change later    
    

def next_round(data,players):
    for player in players:
        turn(data, players, player)
    return players
    
    

    
    
show_data(data, players)
#print(data)
#print(players, len(data[1]))                           

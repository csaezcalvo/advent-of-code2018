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
            players.append(['G',(i,j), 200])
            row.append('.')
        elif x == 'E':
            players.append(['E',(i,j), 200])
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

def shortest_path2(data, players, pos1,pos2):
    #Returns the first step in order of a shortest path from pos1 to pos2
    players_pos = [player[1] for player in players]
    paths = [pos1]
    last_layer=[]
    initial_layer = [(x,y) for x in range(pos1[0]-1,pos1[0]+2)
                 for y in range(pos1[1]-1,pos1[1]+2)
                     if (man_dist(pos1, (x,y)) == 1
                         and data[x][y] == '.'
                         and not((x,y) in players_pos)
                         and not((x,y) in paths))]
    if pos2 in initial_layer:
        return (pos2, 1)
    for i in range(len(initial_layer)):
        paths.append(initial_layer[i-1])
        last_layer.append((initial_layer[i-1],i))
    dead_end=False
    length = 2
    #print(last_layer, paths)
    while not(dead_end):
        #print(paths)
        dead_end = True
        next_layer = []
        for node in last_layer:
            if man_dist(node[0],pos2) == 1:
                #print(initial_layer, node[1], length)
                return (initial_layer[node[1]], length)
            reachable = [((x,y), node[1]) for x in range(node[0][0]-1,node[0][0]+2)
                 for y in range(node[0][1]-1,node[0][1]+2)
                     if (man_dist(node[0], (x,y)) == 1
                         and data[x][y] == '.'
                         and not((x,y) in players_pos)
                         and not((x,y) in paths))]
            if len(reachable)>0:
                dead_end = False
                for point in reachable:
                    next_layer.append(point)
                    paths.append(point[0])
        last_layer = sorted(next_layer)
        length +=1
    return (0,-1)
    
            

#print(shortest_path2(data, players,(17,7), (17,22)))

def turn(data, players, player):
    players = sort(players) #Sort the players by position
    
    if player[0] == 'G':
        enemies = [x for x in players if x[0] == 'E']
    else:
        enemies = [x for x in players if x[0] == 'G']
    #Checks if there are enemies
    if enemies == []:
        return False #Maybe change later
    else:
        moves = []
        for enemy in enemies:
            #print('enemy',enemy)
            x = shortest_path2(data, players, player[1],enemy[1])
            if x[1] == -1:
                return True
            else:
                moves.append(x)
        index = min(range(len(moves)), key = lambda k: moves[k][1])
        move = moves[index]
        if move[1] == 1: #Attack
            enemies[index][2] -= 3
        else:
            player[1] = move[0]
    return True          
    

def next_round(data,players):
    for player in players:
        #print(player)
        turn(data, players, player)
    return players

def battle(data,players):
    next_players = next_round(data,players)
    turn = 1
    print(players)
    print(next_players)
    while (next_players != players):
        print(turn)
        players = next_players
        next_players = players
        turn +=1
    return players

print(shortest_path2(data,players,(7,14),(15,24)))

show_data(data,players)
players = battle(data,players)    
show_data(data, players)
#print(data)
#print(players, len(data[1]))                           

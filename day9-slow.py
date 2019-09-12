players = 431
last_marble = 7095000

scores = {i:0 for i in range(players)}
#print(scores)    

turn = 1
player=0
circle = [0]
current  = 0
while turn <= last_marble:
    if turn%1000 == 0:
        print(turn)
    if turn%23 != 0:
        circle.insert((current+2)%len(circle), turn)
        current = (current+2)%(len(circle)-1)
    else:
        rem = circle.pop((current-7)%len(circle))
        scores[player] += turn + rem
        current = (current-7)%(len(circle)+1)
    if(turn%10==0):
        print(circle)
    turn = 1
    player = (player+1)%players
max_score = max(scores.values())

print(max_score)

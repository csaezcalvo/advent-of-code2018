from collections import deque

players = 431
last_marble = 7095000

scores = {i:0 for i in range(players)}

turn = 1
player=0
circle = deque([0])
while turn <= last_marble:
    if turn%1000 == 0:
        print(turn)
    if turn%23 != 0:
        circle.rotate(-2)
        circle.appendleft(turn)
    else:
        circle.rotate(7)
        x = circle.popleft()
        scores[player] += turn + x
    turn += 1
    player = (player+1)%players
max_score = max(scores.values())

print(max_score)

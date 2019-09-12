import numpy as np
import matplotlib.pyplot as plt

file_path = "/home/carlos/advcode2018/input10"
file = open(file_path,'r')
data = dict()
for line in file:
    p1 = int(line.split(',')[0][-6:])
    p2 = -int(line.split(',')[1][:7])
    v1 = int(line.split(',')[1][-2:])
    v2 = -int(line.split(',')[2][:-2])
    data[(p1,p2)] = (v1,v2)

def update(data,t):
    coords = data.keys()
    new_coords = []
    for (x,y) in coords:
        new_coords.append((x+t*data[(x,y)][0], y + t*data[(x,y)][1]))
    return new_coords

print(update(data,0)[0],update(data,20000)[0] )

t=10645
while t==10645:
    coords = update(data,t)
    coordx = np.array([x[0] for x in coords])
    coordy = np.array([x[1] for x in coords])
    #plt.xlim(-100000,100000)
    #plt.ylim(-100000,100000)
    plt.scatter(coordx,coordy)
    plt.pause(1)
    #plt.clf()
    t +=10
    print(t)


plt.show()

        
    

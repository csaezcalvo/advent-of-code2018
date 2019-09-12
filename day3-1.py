def process(file):
    claims=[]
    data = open(file,'r')
    for line in data:
        claim=[]
        claim.append(int(line.split('@')[1].split(',')[0]))
        claim.append(int(line.split('@')[1].split(',')[1].split(':')[0]))
        claim.append(int(line.split(':')[1].split('x')[0]))
        claim.append(int(line.split(':')[1].split('x')[1]))
        claims.append(claim)
    return claims

file="/home/carlos/advcode2018/input3"
claims = process(file)

def overlap(inp):
    fabric = [[0 for col in range(1000)] for row in range(1000)]
    for x in inp:
        for i in range(x[2]):
            for j in range(x[3]):
                if fabric[x[0]+i][x[1]+j] == 0:
                    fabric[x[0]+i][x[1]+j] = 1
                else:
                    fabric[x[0]+i][x[1]+j] = 2
    return sum([(fabric[i][j] == 2) for i in range(1000) for j in range(1000)])

print(overlap(claims))
        
    

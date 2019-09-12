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

def overlap(claim1,claim2):
    not_x_overlap = (claim1[0]+claim1[2] < claim2[0]) or (claim2[0]+claim2[2] < claim1[0])
    not_y_overlap = (claim1[1]+claim1[3] < claim2[1]) or (claim2[1]+claim2[3] < claim1[1])
    return not(not_x_overlap or not_y_overlap)

def find_no_overlap(claims):
    claim_id=0    
    for i in range(len(claims)):
        claim_id = i+1
        for j in range(len(claims)):
            if (overlap(claims[i],claims[j]) and i!=j):
                claim_id=0
                break
        if claim_id != 0:
            return claim_id

print(find_no_overlap(claims))
            

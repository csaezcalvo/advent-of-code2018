file = "/home/carlos/advcode2018/input"
data = open(file,'r')

lista=[]
x=0
iter = 0
flag = True
while flag:
    print(iter)
    for line in data:
        x += int(line)
        if x in lista:
            print(x)
            flag=False
            break
        else:
            lista.append(x)
    data.seek(0)
    iter += 1
        

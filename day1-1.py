total = 0
file = "/home/carlos/advcode2018/input"
data = open(file,'r')
for line in data:
    total += int(line)

print(total)

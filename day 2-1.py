file = "/home/carlos/advcode2018/input2"
data = open(file,'r')

two = 0
three = 0
for word in data:
    for x in word:
        if word.count(x) == 2:
            two += 1
            break
    for x in word:
        if word.count(x) == 3:
            three += 1
            break

print(two*three)

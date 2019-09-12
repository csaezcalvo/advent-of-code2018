import time

initial = [3,7]
i = 0
j = 1
num_recipes = 323081

def new_recipes(recipe,i,j):
    new = recipe[i] + recipe[j]
    if len(str(new))==1:
        recipe.append(new)
    else:
        recipe.append(new//10)
        recipe.append(new%10)
    i = (i+1+recipe[i])%len(recipe)
    j = (j+1+recipe[j])%len(recipe)
    return (recipe,i,j)

def iterate(num_recipes):
    recipe = [3,7]
    i = 0
    j = 1
    while len(recipe) < num_recipes + 10:
        (recipe,i,j) = new_recipes(recipe,i,j)
    return ''.join([str(x) for x in recipe[-10:]])

def find_before(num):
    goal = [int(x) for x in list(num)]
    recipe = [3,7]
    i = 0
    j = 1
    it=0
    while True:
        if len(recipe)>=len(goal):
            if recipe[-len(goal):] == goal:
                return len(recipe[:-len(goal)])
            if recipe[-len(goal)-1:-1] == goal:
                return len(recipe[:-len(goal)-1])
        (recipe,i,j) = new_recipes(recipe,i,j)
        it +=1
        if it % 1000000 == 0:
            print(it, len(recipe))
    
x = [1,2,3,4,5]
print(x[-4:-1])

start = time.time()
print(find_before('323081'))
end = time.time()
print(end-start)
#print(iterate(num_recipes))

    

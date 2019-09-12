file ="/home/carlos/advcode2018/input6"
data = open(file,'r')

def process_data(data):
    coord = []
    for line in data:
        coord.append((int(line.split(',')[0]), int(line.split(',')[1])))
    return coord

def man_dist(point1,point2):
    return abs(point1[0] - point2[0]) + abs(point1[1]-point2[1])

def closest_point(coords, point):
    closest  = coords[0]
    clos_dist = man_dist(closest,point)
    for x in coords[1:]:
        dist = man_dist(x, point)
        if dist < clos_dist:
            closest = x
            clos_dist = dist
        elif dist == clos_dist:
            closest = 0
    return closest

def max_area(coords):
    min_grid=min([x[0] for x in coords] + [x[1] for x in coords])
    max_grid=max([x[0] for x in coords] + [x[1] for x in coords])
    count = {key:0 for key in coords}
    for x in range(min_grid, max_grid):
        for y in range(min_grid, max_grid):
            point = closest_point(coords, (x,y))
            if point != 0:
                count[point] += 1
    #Elimminate infinite area points (border points)
    for x in range(min_grid, max_grid):
        count[closest_point(coords, (x,min_grid))] = 0
        count[closest_point(coords, (x,max_grid))] = 0
    for y in range(min_grid, max_grid):
        count[closest_point(coords, (min_grid,y))] = 0
        count[closest_point(coords, (max_grid,y))] = 0
    return max(count.values())

#Part 2

def total_dist(coords, point, bound):
    # If total_dist > bound it returns -1
    total = 0
    for x in coords:
        total += man_dist(x, point)
        if total >= bound:
            return -1
    return total

def area(coords, bound):
    area=0
    min_grid=min([x[0] for x in coords] + [x[1] for x in coords])
    max_grid=max([x[0] for x in coords] + [x[1] for x in coords])
    for x in range(min_grid, max_grid):
        for y in range(min_grid, max_grid):
            if total_dist(coords, (x,y), bound) != -1:
                area += 1
    return area

coords = process_data(data)
#coords =  [(1, 1),(1, 6),(8, 3),(3, 4),(5, 5),(8, 9)]

print(area(coords,10000))

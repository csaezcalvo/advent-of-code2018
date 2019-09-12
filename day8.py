file_path = "/home/carlos/advcode2018/input8"
file = open(file_path,'r')
for line in file:
    data = line.split(' ')

def process_tree(data):
    tree = dict()
    i=0
    while i < len(data):
        num_nodes = data[i]
        num_metadata = data[i+1]

def compute_tree(data, node):
    tree = dict()
    num_nodes = data[node]
    num_metadata = data[node+1]
    if num_nodes == 0:
        tree[node] = [[], data[node+2:node+2+num_metadata]]
        end_of_tree = node+2+num_metadata
        return (tree, end_of_tree)
    ind = node+2
    childs = []
    metadata = []
    for i in range(num_nodes):
        childs.append(ind)
        tree = {**tree, **compute_tree(data,ind)[0]}
        ind = compute_tree(data,ind)[1]
    end_of_tree = ind+num_metadata
    metadata = data[ind:end_of_tree]
    tree[node] = [childs, metadata]
    return (tree, end_of_tree)

def sum_metadata(tree):
    total = 0
    for (x,y) in tree.items():
        total += sum(y[1])
    return total

#Part 2

def node_value(tree, node):
    childs = tree[node][0]
    metadata = tree[node][1]
    if len(childs) == 0:
        return sum(metadata)
    value=0
    for i in metadata:
        if i-1 < len(childs):
            value += node_value(tree, childs[i-1])
    return value
        
    

data = [int(x) for x in data]
#data = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]
    
tree = compute_tree(data,0)[0]
print(node_value(tree,0))        
        


        
        
    


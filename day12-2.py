#file_path = "/home/carlos/advcode2018/input12"
#file = open(file_path,'r')
import time

initial_input = "##.##..#.#....#.##...###.##.#.#..###.#....##.###.#..###...#.##.#...#.#####.###.##..#######.####..#"
rules = {".##..": '#', '#...#': '.', '####.': '#', '##..#': '#','..##.': '.', '.###.': '.',
         '..#.#': '.', '#####':'.','##.#.':'#', '...##':'#', '.#.#.':'.',
         '##.##':'#', '#.##.':'.', '#....':'.', '#..##':'.', '..#..':'#',
         '.#..#':'#', '.#.##':'#', '...#.':'.', '.#...':'#', '###.#':'#',
         '#..#.':'#', '.####':'#', '#.###':'#', '.##.#':'#', '#.#..':'.',
         '###..':'#', '.....':'.', '##...':'.', '....#':'.', '#.#.#':'#', '..###':'#'}

def process_input(inp):
    return [x for x in range(len(inp)) if inp[x] == '#']

def context(inp, i):
    l = len(inp)        
    ctxt = list('....#....')
    if i<4:
        mn = i
    else:
        mn=4
    if i>l-5:
        mx= l-i
    else:
        mx = 5
        
    rel_pos = [x-inp[i] for x in inp[i-mn:i+mx] if (inp[i]-x<=4 and inp[i]-x>=-4)]
    #print(mn,mx,rel_pos)
    for j in rel_pos:
        ctxt[j+4] = '#'
    return ''.join(ctxt)


def next_iter(inp, rules):
    new_inp = []
    for i in range(len(inp)):
        ctxt = context(inp,i)
        #print(ctxt)
        if i == len(inp)-1 or inp[i+1]-inp[i]>4:
            top = 3
        elif inp[i+1]-inp[i]==4:
            top = 2
        else:
            top=1
        if i==0 or inp[i] - inp[i-1] > 2:
            bottom = -2
        else:
            bottom = inp[i-1] - inp[i]+1
        for j in range(bottom,top):
            if rules[ctxt[4+j-2:4+j+3]]=='#':
                new_inp.append(inp[i]+j)
        #print(i,new_inp)
    return new_inp        

def iterate(inp, num_iters):
    #new_inp = inp
    for i in range(num_iters):
        new_inp = next_iter(inp, rules)
        shift = min(new_inp) - min(inp)
        if new_inp == [x+shift for x in inp]:
            print(i,'hey!')
            return [x+shift*(num_iters-i) for x in inp] 
        inp = new_inp
        if i%1000 == 0:
            print(i)
    return new_inp

def total_plants(inp):
    return sum(inp)

num_iter = 50000000000
inp=process_input(initial_input)
#print(inp)
#print(next_iter(inp,rules))
print(total_plants(iterate(inp,num_iter)))
#print(iterate(inp,num_iter))




#file_path = "/home/carlos/advcode2018/input12"
#file = open(file_path,'r')

initial_input = "##.##..#.#....#.##...###.##.#.#..###.#....##.###.#..###...#.##.#...#.#####.###.##..#######.####..#"
rules = {".##..": '#', '#...#': '.', '####.': '#', '##..#': '#','..##.': '.', '.###.': '.',
         '..#.#': '.', '#####':'.','##.#.':'#', '...##':'#', '.#.#.':'.',
         '##.##':'#', '#.##.':'.', '#....':'.', '#..##':'.', '..#..':'#',
         '.#..#':'#', '.#.##':'#', '...#.':'.', '.#...':'#', '###.#':'#',
         '#..#.':'#', '.####':'#', '#.###':'#', '.##.#':'#', '#.#..':'.',
         '###..':'#', '.....':'.', '##...':'.', '....#':'.', '#.#.#':'#', '..###':'#'}

def next_iter(inp, first_index):
    first_index -= 2
    extra = '....'
    inp = extra + inp + extra
    new_inp = []
    for i in range(2,len(inp)-3):
        if rules[inp[i-2:i+3]] == '#':
            new_inp.append('#')
        else:
            new_inp.append('.')
    return (''.join(new_inp), first_index)
            

def iterate(input, num_iters):
    first_index = 0
    for i in range(num_iters):
        if i%100 == 0:
            print(i)
        (input, first_index) = next_iter(input, first_index)
    return (input, first_index)

def total_plants(inp, first_index):
    return sum([first_index + i for i in range(len(inp)) if inp[i] == '#'])

num_iter = 20
#print(total_plants(*iterate(initial_input, num_iter)))
x = next_iter(initial_input, 0)[0]
print(len(x),x)

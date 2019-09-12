file = "/home/carlos/advcode2018/input"
data = open(file,'r')

def first_repeated_freq(data):
    set_of_freq=set()
    length = len(set_of_freq)
    freq = 0
    while True:
        for line in data:
            freq += int(line)
            set_of_freq.add(freq)
            if length == len(set_of_freq):
                print('done!')
                return freq
            else:
                length = len(set_of_freq)
        data.seek(0)

print(first_repeated_freq(data))

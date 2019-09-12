file = "/home/carlos/advcode2018/input7"
data = open(file,'r')

def process(data):
    inst = {key:[] for key in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'}
    for line in data:
        step1 = line.split(' ')[1]
        step2 = line.split(' ')[-3]
        inst[step2].append(step1)
    return inst

def elim(inst, step):
    return {key:[x for x in inst[key] if x != step] for key in inst.keys()} 

def order_of_steps(inst):
    order=''
    while len(order) < len(inst.keys()):
        for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if (not(l in order) and len(inst[l])==0):
                order += l
                inst = elim(inst, l)
                break
    return order

def total_time(inst, workers):
    step_time = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ',range(61,61+27)))
    time=0
    work_time = [0 for x in range(workers)]
    work_job = ['' for x in range(workers)]
    done=''
    while len(done) < len(inst.keys()):
        if work_time != [0 for x in range(workers)]:
            passed = min([x for x in work_time if x != 0])
            time += passed
            for i in range(workers):
                if work_time[i] != 0:
                    work_time[i] -= passed        
                    
        for i in range(workers):
            if work_job[i] != '' and work_time[i] == 0:
                done += work_job[i]
                inst = elim(inst, work_job[i])
                work_job[i]=''        
        
        for l in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            if (not((l in done)) and len(inst[l])==0) and not(l in work_job) and 0 in work_time:
                ind = work_time.index(0)
                work_time[ind] = step_time[l]
                work_job[ind] = l
    return time
                
                


inst = process(data)
#inst = {'A':['C'], 'B':['A'], 'C':[], 'D':['A'], 'E':['B','D','F'], 'F':['C']}
print(order_of_steps(inst))
print(total_time(inst, 5))


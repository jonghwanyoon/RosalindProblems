#
# [DDEG	Double-Degree Array]
#
#


def DDEG(data_file):
    with open(data_file) as f:
        n, e = f.readline().strip('\n').split(' ')
        n = int(n)
        e = int(e)
        dic = {i:[] for i in range(1,n+1)}
        line = f.readline()
        while line:
            d1, d2 = line.strip('\n').split(' ')
            d1 = int(d1)
            d2 = int(d2)
            dic[d1].append(d2)
            dic[d2].append(d1)
            line = f.readline()
    
    return [sum([len(dic[node]) for node in dic[k]]) for k in range(1,n+1)]

with open('output.tsv', 'w') as w:
    w.write(' '.join([str(i) for i in DDEG('input.tsv')]))
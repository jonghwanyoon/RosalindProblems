#
# [BA3E Construct the De Bruijn Graph of a Collection of k-mers]
#

def BA3E(Patterns):
    dic={}
    for p in Patterns:
        sub1 = p[:-1]
        sub2 = p[1:]
        if sub1 not in dic:
            dic[sub1] = []
        dic[sub1].append(sub2)
    for k in sorted(list(dic.keys())):
        print('{} -> {}'.format(k, ','.join(sorted(dic[k]))))
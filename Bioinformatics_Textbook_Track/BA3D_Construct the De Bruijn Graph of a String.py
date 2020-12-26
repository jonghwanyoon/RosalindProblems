#
# [BA3D Construct the De Bruijn Graph of a String]
#

def BA3D(k, Text):
    dic = {}
    for i in range(0,len(Text)-k+1):
        sub1 = Text[i:i+(k-1)]
        sub2 = Text[i+1:i+k]
        if sub1 not in dic:
            dic[sub1]=[]
        dic[sub1].append(sub2)
    for k in sorted(list(dic.keys())):
        print('{} -> {}'.format(k, ','.join(sorted(dic[k]))))

#
# [BA3H Reconstruct a String from its k-mer Composition]
#
def BA3H(k, Patterns):
    dic={}
    suffix = []
    for p in Patterns:
        sub1 = p[:-1]
        sub2 = p[1:]
        if sub1 not in dic:
            dic[sub1] = []
        suffix.append(sub2)
        dic[sub1].append(sub2)
    for k in dic.keys():
        if k not in suffix:
            sub = k
            break
    out = sub
    while True:
        if sub not in dic:
            break
        sub = dic[sub][0]
        out += sub[-1]
    return out
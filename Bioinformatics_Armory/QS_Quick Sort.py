#
# [QS Quick Sort]
#
def QS(A, n=None):
    if type(A[0])!= list:
        A = [A]
    lst = []
    for n, subA in enumerate(A):
        if len(subA)==0:
            continue
        e = subA[0]
        lst.append([i for i in subA if i < e ])
        lst.append([e for _ in range(subA.count(e))])
        lst.append([i for i in subA if i>e])
    if A == lst:
        out = []
        for i in lst:
            out += i 
        return out
    else:
        return QS(lst)
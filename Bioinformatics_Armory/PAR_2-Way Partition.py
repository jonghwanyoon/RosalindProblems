#
# [PAR 2-Way Partition]
#
def PAR(n, A):
    e = A[0]
    return [i for i in A if i < e ] + [e for _ in range(A.count(e))] + [i for i in A if i>e] 
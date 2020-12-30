#
# [PAR3 3-Way Partition]
# 2-way랑 같은 코드임.
def PAR3(n, A):
    e = A[0]
    return [i for i in A if i < e ] + [e for _ in range(A.count(e))] + [i for i in A if i>e] 
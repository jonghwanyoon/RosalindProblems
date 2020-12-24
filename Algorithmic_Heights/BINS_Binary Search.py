#
# [BINS	Binary Search]
#


def BINS(n, m, A, k):
    return ' '.join([str(A.index(k[i])+1) if k[i] in A else '-1' for i in range(m)])

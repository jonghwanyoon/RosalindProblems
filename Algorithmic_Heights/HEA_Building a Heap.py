#
# [HEA Building a Heap]
#
def HEA(A : list, n : int) -> list:
    while True:
        flag = True
        for idx in range(n-1, 0, -1):
            p_idx = int((idx + idx%2)/2-1)
            child = A[idx]
            parent = A[p_idx]
            if child > parent:
                A[idx] = parent
                A[p_idx] = child
                flag = False
        if flag:
            break
    return A
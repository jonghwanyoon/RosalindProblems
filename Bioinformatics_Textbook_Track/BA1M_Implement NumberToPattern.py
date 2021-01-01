#
# [BA1M Implement NumberToPattern]
#
def BA1M(index : int, k : int) -> str:
    base = ['A', 'C', 'G', 'T']
    b    = '{:b}'.format(index)
    b    = '0' * (k*2 - len(b)) + b
    return ''.join([base[idx] for idx in [int(b[i:i+2],2) for i in range(0, k*2, 2)]])
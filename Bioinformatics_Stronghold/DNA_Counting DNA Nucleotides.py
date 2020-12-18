#
# 주어진 DNA sequence에서 base counts를 반환하면 됨.
#

def base_counts(seq):
    return(' '.join([str(seq.count(base)) for base in ['A', 'C', 'G', 'T']]))

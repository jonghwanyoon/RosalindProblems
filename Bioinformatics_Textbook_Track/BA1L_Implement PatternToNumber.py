#
# [BA1L Implement PatternToNumber]
#

def BA1L(Pattern):
    bases = ['A', 'C', 'G', 'T']
    return int(''.join([str(bases.index(base)) for base in Pattern]),4)
#
# [BA1N Generate the d-Neighborhood of a String]
#
def GET_KMER(k, base=['A','C','G','T']):
    if len(base[0])==k:
        return base
    else:
        return GET_KMER(k, base=[base1+base2 for base1 in base for base2 in ['A','C','G','T']])

def BA1N(Pattern, d):
    from itertools import combinations as comb
    main = []
    total = len(Pattern)
    iters = comb(range(total), d)
    kmer_set = GET_KMER(d)
    for i in iters:
        lst = list(Pattern)
        for kmer in kmer_set:
            kmer = list(kmer)
            for idx in range(len(i)):
                lst[i[idx]] = kmer[idx]
            if ''.join(lst) not in main:
                main.append(''.join(lst))
    return main
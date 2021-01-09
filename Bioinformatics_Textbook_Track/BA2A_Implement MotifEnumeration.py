#
# [BA2A Implement MotifEnumeration]
#
def GET_KMER(k, base=['A','C','G','T']):
    if len(base[0])==k:
        return base
    else:
        return GET_KMER(k, base=[base1+base2 for base1 in base for base2 in ['A','C','G','T']])

def HAMM(s,t):
    return len([i for i in range(len(s)) if s[i]!=t[i]])

def BA2A(k : int, d : int, Dna : list) -> list:
    kmer_set = GET_KMER(k)
    Patterns = []
    for seq in Dna:
        Pattern = []
        for i in range(len(seq)-k+1):
            subseq = seq[i:i+k]
            for kmer in kmer_set:
                if HAMM(kmer, subseq) <= d:
                    Pattern.append(kmer)
        Patterns.append(set(Pattern))
    out = Patterns[0]
    for i in range(1, len(Patterns)):
        out = out.intersection(Patterns[i])
    return sorted(list(out))
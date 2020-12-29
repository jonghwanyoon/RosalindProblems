#
# [BA1J Find Frequent Words with Mismatches and Reverse Complements]
#
def REVC(seq):
    dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join(reversed([dic[base] for base in seq]))

def GET_KMER(k, base=['A','C','G','T']):
    if len(base[0])==k:
        return base
    else:
        return GET_KMER(k, base=[base1+base2 for base1 in base for base2 in ['A','C','G','T']])

def BA1I(Text, k, d):
    kmer_lst = GET_KMER(k)
    dic = {i:0 for i in kmer_lst}
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        revc = REVC(kmer)
        for kmer2 in dic:
            hamm = len([None for idx in range(len(kmer)) if kmer[idx]!=kmer2[idx]])
            if hamm <= d:
                dic[kmer2]+=1
            hamm = len([None for idx in range(len(revc)) if revc[idx]!=kmer2[idx]])
            if hamm <= d:
                dic[kmer2]+=1
    maximum = max(dic.values())
    return [kmer for kmer in dic if dic[kmer]==maximum]
#
# [ORFR Finding Genes with ORFs]
#

def ORFR(s):
    revcomp = lambda x: {"A":"T", "T":"A", "C":"G", "G":"C"}[x]
    from Bio import Seq
    n = len(s)
    s_rev = ''.join(map(revcomp, s[::-1]))
    max_orf = ''
    for sequence in [s, s_rev, s[::-1], s_rev[::-1]]:
        for pos in range(3):
            codons = [sequence[i:i+3] for i in range(pos,n,3) ]
            stops = []
            if 'ATG' not in codons:
                continue
            start = codons.index('ATG')
            if 'TAG' in codons[start:]: 
                stops.append(codons.index('TAG', start))
            if 'TAA' in codons[start:]:
                stops.append(codons.index('TAA', start))
            if 'TGA' in codons[start:]:
                stops.append(codons.index('TGA', start))
            if len(stops)==0:
                continue
            try:
                stop = min([i for i in stops if i > start])
            except:
                continue
            seq = codons[start:stop]
            orf = Seq.translate(''.join(seq))
            if len(orf) > len(max_orf):
                max_orf = orf

    return max_orf

# s = 'CAGCAATCCTAGGTTAGGGATGGACGCCGCCTATAATACTCGGCTGTTGCCCGTTATTACGTTGCACCCCATTTCACCAGACGTAGTACCTACAAACCTCCGGGCTTGAGAGTCGCATGATTGGTGCATCAGGCTTGACGGAGTTTCCGGAGCCCAGGTCTTAAAAGACTTACTACGCCCACTTATATCTTTATGTTGGCAACGAATACACCAATGTGACGCCCCACGCTGACACGTTCCCGGAATACGGCCTCACTGAATCTTGTGTAGTGGCCCTCAATCTTGGCGCATCAAGCGCACTGCCTAGCACCAAGGCCCCAGTGCCTGCATACCTTCGACTGGCGTGAACCGGAGAGAGTTCATACAACATTATCGGGAACTGCTCACGGATAAAGTTTGACGAGTATGCTTGCGGGCTTGCGGCCCTAGCTAGGGCCGCAAGCCCGCAAGCATTGTTACGAATTAATCGTGCCAAGGCAAACGTTACGCGAACAACCAGATCAGCCCGCCATTGTGGCACCATCGTCCAACACTCAAGATGATTCAGCCTAGTTCGCTTGGTCATACCCTGTTACGGTGGCCGTGCTGCCTTCGCATGGAACGCAAGAGCGCGGAGCTTACGTAGGAGGACGTATTCGGTTAGGCCATTCTATCACGGTTGACGGCTGACTTGCAAGTCGAGTAATCGGAGTGTTCACTCGTCTGAGATGCTAACGGGAATAGTAGATCAAGGTGACAACGGCAGGACGCAGCAAAACTACCTTGGGTTCGGTGCTCCCCGCACGTGTATGGGACTTTACCCAATTACTTAACTCGTTCTCGACTTCTTGCCTGAGACTCGCACGCGTTGAACATCGA'
# print(ORFR(s))

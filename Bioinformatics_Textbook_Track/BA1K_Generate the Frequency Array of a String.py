#
# [BA1K Generate the Frequency Array of a String]
#

def BA1K(Text, k):
    bases = ['A', 'C', 'G', 'T']

    for i in range(k-1):
        bases = [base+j for base in bases for j in ['A', 'C', 'G', 'T']]
    dic = {base:0 for base in bases}
    for i in range(len(Text)-k+1):
        kmer = Text[i:i+k]
        dic[kmer]+=1
    print(' '.join([str(dic[base]) for base in bases]))

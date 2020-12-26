#
# [BA3A Generate the k-mer Composition of a String]
# DNA string에서 나올 수 있는 k-mer를 반환하면 됨.
#

def BA3A(k, Text):
    kmer = []
    for i in range(0, len(Text)-k+1):
        substring = Text[i:i+k] 
        if substring not in kmer:
            kmer.append(substring)
    return sorted(kmer)
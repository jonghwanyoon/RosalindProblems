#
# [BA2B Find a Median String]
#

def BA2B(k, DNA):
    dic = {}
    for dna in DNA:
        for i in range(len(dna)-k+1):
            kmer = dna[i:i+k]
            if kmer not in dic:
                dic[kmer] = 0
            dic[kmer]+=1
    return sorted([[k, dic[k]] for k in dic.keys()], key=lambda x: x[1], reverse=True)[0][0]

data = [line.strip('\n') for line in open('input.tsv')]
k = int(data[0])
DNA =  data[1:]
print(BA2B(k,DNA))
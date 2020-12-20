#
# 주어진 DNA sequence 에서 consensus string을 반환하면 됨.
#
#

def CONS(fasta):
    from Bio import SeqIO
    parser = SeqIO.parse(fasta, format='fasta')
    dic = None
    bases = ['A', 'C', 'G', 'T']
    for record in parser:
        seq = list(record.seq)
        if dic == None:
            dic = {base:[0 for _ in seq] for base in bases}
        for i,base in enumerate(seq):
            dic[base][i] += 1
    
    concensus = ''
    for i in range(len(seq)):
        counts = [dic[base][i] for base in bases]
        concensus += bases[counts.index(max(counts))]
    print(concensus)
    for base in bases:
        print('{base}: {count}'.format(base=base, count=' '.join(list(map(str,dic[base])))))
        
#
# Fasta format으로 주어짐.
# 가장 높은 GC content를 가진 ID와 GC content(%) 를 반환하면 됨
#
def GC(fasta):
    from Bio import SeqIO
    parser = SeqIO.parse(fasta, format='fasta')
    max_dic = {'ID' : None, 'GC':0}
    for record in parser:
        seq = record.seq
        GC  = round((seq.count('G') + seq.count('C')) / len(seq) * 100 , 6)
        if GC > max_dic['GC']:
            max_dic['GC'] = GC
            max_dic['ID'] = record.id
        
    return max_dic

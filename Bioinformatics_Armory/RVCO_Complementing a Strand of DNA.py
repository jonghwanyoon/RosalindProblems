#
# DNA sequence 들이 Fasta format으로 주어지고 
# 각 sequence 중 Reverse complement와 일치하는게 몇개인지 반환하면 됨.
#


def RVCO(fasta):
    from Bio import SeqIO
    parser = SeqIO.parse(fasta, format='fasta')
    c = 0
    for record in parser:
        seq = record.seq
        rvco = seq.reverse_complement()
        if seq == rvco:
            c+=1
    return c

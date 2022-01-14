#
# [PMCH_Perfect Matchings and RNA Secondary Structures]
# A, U 는 같은 count로 있고 G,C도 같다는게 중요함.

def PMCH(fasta):
    from Bio import SeqIO
    from math import factorial
    parser = SeqIO.parse(fasta, format='fasta')
    AU = 0
    GC = 0 
    for record in parser:
        seq = str(record.seq)
        for base in seq:
            if base == "A":
                AU += 1
            elif base == "C":
                GC += 1
    
    return factorial(AU) * factorial(GC)

print(PMCH("sequence.fasta"))
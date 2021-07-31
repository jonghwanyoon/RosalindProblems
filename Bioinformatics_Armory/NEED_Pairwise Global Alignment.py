#
# [NEED	Pairwise Global Alignment]
#

def NEED(ID1, ID2):
    from Bio import Entrez, SeqIO, pairwise2
    import subprocess
    Entrez.email='example@mail.com'
    handle = Entrez.efetch(db='nucleotide', id=[ID1, ID2], rettype='fasta')
    records = list(SeqIO.parse(handle, "fasta"))
    print(pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])

# NEED('JX205496.1', 'JX469991.1')

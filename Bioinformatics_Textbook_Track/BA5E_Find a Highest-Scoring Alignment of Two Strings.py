

def BA5E(string):
    seq1 = string[0]
    seq2 = string[1]
    from Bio import Entrez, SeqIO, pairwise2
    from Bio.SubsMat import MatrixInfo as matlist
    # handle = Entrez.efetch(db='nucleotide', id=[ID1, ID2], rettype='fasta')
    # records = list(SeqIO.parse('input.tsv', format='fasta'))
    # pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])
    matrix = matlist.blosum62
    for a in pairwise2.align.globaldx(seq1, seq2, matrix):
        print(pairwise2.format_alignment(*a))

string = """PLEASANTLY
MEANLY""".split('\n')
BA5E(string)
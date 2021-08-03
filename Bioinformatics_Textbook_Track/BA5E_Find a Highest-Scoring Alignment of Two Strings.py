

def BA5E(string):
    seq1 = string[0]
    seq2 = string[1]
    from Bio import pairwise2
    from Bio.SubsMat import MatrixInfo as matlist
    # handle = Entrez.efetch(db='nucleotide', id=[ID1, ID2], rettype='fasta')
    # records = list(SeqIO.parse('input.tsv', format='fasta'))
    # pairwise2.align.globalms(records[0].seq, records[1].seq, 5, -4, -10, -1)[0][2])
    matrix = matlist.blosum62
    align_dic = {}
    for a in pairwise2.align.globalds(seq1, seq2, matrix, -5, -5):
        gaps = 0
        align1, _, align2, score, _ = (pairwise2.format_alignment(*a).split('\n'))
        gaps += align1.count('-')
        gaps += align2.count('-')

        score = int(score.split('=')[1])

        if score not in align_dic:
            align_dic[score] = []
        align_dic[score].append([align1, align2])
    
    max_score = max(align_dic)
    print(max_score)
    print(align_dic[max_score][0][0])
    print(align_dic[max_score][0][1])

# string = """PLEASANTLY
# MEANLY""".split('\n')
# BA5E(string)
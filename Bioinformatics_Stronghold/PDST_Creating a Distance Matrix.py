#
# 주어진 taxa n개에 대한 p-distance matrix를 만드는 문제.
# matrix 부분에서 최적화가 더 가능할것으로 보이지만 추후 수정.
#

def pDist(s1, s2):
    total = len(s1)
    diff = 0
    for i, b1 in enumerate(s1):
        b2 = s2[i]
        if b1 != b2:
            diff += 1
    return f"{(diff / total):.5f}"

def PDST(input_file, output_file):
    from Bio import SeqIO
    parser = SeqIO.parse(input_file, format = "fasta")

    # Get sequences
    seqs = [str(record.seq) for record in parser.records]

    # Make matrix
    matrix = [[pDist(s1,s2) for s2 in seqs] for s1 in seqs]
    
    # Write
    with open(output_file, "w") as w:
        for row in matrix:
            w.write(" ".join(row) + "\n")

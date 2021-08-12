#
# [BA5C Find a Longest Common Subsequence of Two Strings]
#  - LCSQ Finding a Shared Spliced Motif와 같은 문제임
#


def LCSLength(seq1, seq2):
    seq1 = '0'+ seq1
    seq2 = '0'+ seq2
    m = len(seq1)
    n = len(seq2)
    A = [[None for _ in range(n)] for _ in range(m)]
    for i in range(m):
        A[i][0] = 0
    for j in range(n):
        A[0][j] = 0
    for i in range(1,m):
        for j in range(1,n):
            if seq1[i] == seq2[j]:
                A[i][j] = A[i-1][j-1] + 1
            else:
                A[i][j] = max(A[i][j-1], A[i-1][j])
    return A


def traceback(A, seq1, seq2, i, j):
    if i==0 or j==0:
        return ''
    if seq1[i] == seq2[j]:
        return traceback(A, seq1, seq2, i-1, j-1) + seq1[i]
    if A[i][j-1] > A[i-1][j]:
        return traceback(A, seq1, seq2, i, j-1)
    return traceback(A, seq1, seq2, i-1, j)


def tracebackAll(A, seq1, seq2, i, j):
    if i==0 or j ==0:
        return {""}
    if seq1[i] == seq2[j]:
        return {z+seq1[i] for z in tracebackAll(A, seq1, seq2, i-1, j-1)}
    R = set()
    if A[i][j-1] >= A[i-1][j]:
        R = R.union(tracebackAll(A, seq1, seq2, i, j-1))
    if A[i][j-1] >= A[i-1][j]:
        R = R.union(tracebackAll(A, seq1, seq2, i-1, j))
    return R


def BA5C(fasta):
    import sys
    from Bio import SeqIO
    sys.setrecursionlimit(2000)
    records = list(SeqIO.parse(fasta, "fasta"))
    seq1 = records[0].seq
    seq2 = records[1].seq

    A = LCSLength(seq1, seq2)
    LCS = traceback(A, '0' + seq1, '0'+seq2, len(seq1), len(seq2))
    return LCS


# print(BA5C('input.tsv'))
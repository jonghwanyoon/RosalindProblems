#
# 주어진 DNA sequence의 Reverse Complement를 구하는 문제
#

def get_revc(seq):
    rev_dic = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return ''.join([rev_dic[base] for base in seq[::-1]])
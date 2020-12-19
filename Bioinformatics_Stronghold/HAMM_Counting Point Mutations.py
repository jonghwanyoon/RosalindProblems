#
# 두 개의 DNA sequence s와 t가 주어지고, Hamming Distance를 구하는 문제.
# 여기서는 s,t는 같은 길이로 주어진다.
#

def HAMM(s,t):
    return len([i for i in range(len(s)) if s[i]!=t[i]])

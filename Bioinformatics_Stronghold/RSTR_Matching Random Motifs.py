
#
# DNA s 와 같은 길이의 random dna string N개는 GC-content x 확률로 생성된다. 그중 최소 한개가 s와 완전히 일치할 확률은?
# 최소 1개가 s와 일치할 확률 = 1 - 아무것도 N과 일치하지 않을 확률 ??
# 
# TODO 정확한 통계원리 파악
# 다음 reference를 참고함 http://saradoesbioinformatics.blogspot.com/2016/08/matching-random-motifs.html
#

def RSTR(N, x, s):
    AT = 0
    GC = 0
    for i in s:
        if i in 'GC':
            GC += 1
        else:
            AT += 1
    print(round(1-(1- ((1-x)/2)**AT * ((x)/2)**GC)**N ,3))
    
# n = 90000
# gc = 0.6
# s = 'ATAGCCGA'
# RSTR(n,gc,s)
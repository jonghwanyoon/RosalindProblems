
#
# k-th 세대에서 최소한 N개의 Aa Bb 개체가 있을 확률은?
# k번째 세대는 모집단 P (2^k) 의 개체가 있고 그중 Aa Bb를 가진 개체가 N개 이상인 확률.
# bionormial distribution을 이용해서, P 에서 N 이상인 애들에서 확률을 sum 
#
#          A        a
# A  AA(1/4)  Aa(1/4)
# a  Aa(1/4)  aa(1/4)
#          B        b
# B  BB(1/4)  Bb(1/4)
# b  Bb(1/4)  bb(1/4)
# Aa(1/2) Bb(1/2) -> 1/4
#


def LIA(k, N):
    from math import factorial as fc
    from itertools import combinations as cb
    P = 2**k
    p = 0.25
    prob = 0
    for i in range(N, P+1):
        f = fc(P)/(fc(i)*fc(P-i))
        cur_prob = f*(p**i)*((1-p)**(P-i))
        prob += cur_prob
    print(round(prob, 3))

# LIA(2,1)
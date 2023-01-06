
"""
S1과 S2의 원소들 각각 차이의 절대값중 가장 빈도가 높은 (x가 최대가 되는) 것의 개수와 값을 출력하는 문제
"""

def CONV(S1: list, S2: list):
    from collections import defaultdict
    set_dic = defaultdict(int)
    for s1 in S1:
        for s2 in S2:
            set_dic[round(abs(s1 - s2), 5)] += 1

    value, x= sorted([[k,v ] for k,v in set_dic.items()], key = lambda x: x[1], reverse=True)[0]
    print(x)
    print(value)
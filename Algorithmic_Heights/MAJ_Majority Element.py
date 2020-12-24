
#
# [MAJ	Majority Element]
# n개 element가 있는 array k개가 주어지고, 각 array에서 가장 빈도가 높은 element를 반환해야 하는데,
# 빈도가 n/2 보다 높아야 하고, 아니면 -1을 반환하면 됨.
#


def MAJ(n, k, A):
    lst = []
    for k in A:
        dic = {}
        for element in k:
            if element not in dic:
                dic[element] = 0
            dic[element] += 1 
        total = sum(dic.values())
        major_element, count = sorted([[k,dic[k]] for k in dic], key=lambda x: x[1], reverse=True)[0]
        if count/total <=0.5:
            major_element = -1
        lst.append(str(major_element))
    return lst

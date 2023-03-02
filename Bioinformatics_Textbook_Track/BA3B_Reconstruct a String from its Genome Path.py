#
# [BA3B Reconstruct a String from its Genome Path]
# 
# 문제는 K-mer로 된 서열이 n개 주어지며 i의 (1, K) 글자는 i+1의 (0, K-1)과 일치함.
# 모두 나란히 이어져 있음을 알고 있다면 BA3B로 쉽게 해결이 된다.
#
# 하지만, Genome Path로 String을 재구축 하는 것이 목적이고, 실제에서는 이런 경우는 거의 없다.
# BA3C 이후로 관련 문제가 계속해서 나타난다.

def BA3B(DNA_list):
    return DNA_list[0] + ''.join([DNA_list[i][-1] for i in range(1, len(DNA_list))])

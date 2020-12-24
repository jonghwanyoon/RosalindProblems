#
# [BA9B	Implement TrieMatching]
# 첫 줄에 Text가 주어지고 다음 줄 부터 Text의 Pattern이 주어짐.
# Text에 존재하는 모든 Pattern의 위치를 순서대로 반환하면 됨.
#

def BA9B(Text, Patterns):
    lst = []
    for sub in Patterns:
        idx = 0
        while True:
            pos = Text.find(sub, idx)
            if pos != -1:
                lst.append(pos)
                idx = pos+1
            else:
                break
    
    return sorted(lst)
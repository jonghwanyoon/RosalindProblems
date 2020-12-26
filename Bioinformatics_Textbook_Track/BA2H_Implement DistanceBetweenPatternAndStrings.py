#
# [BA2H	Implement DistanceBetweenPatternAndStrings]
# Pattern과 space seperated DNA string이 주어지고, 각 DNA string의 최소 hamming distance를 합산해서 반환하면 됨.
#

def BA2H(Pattern, DNA):
    n = 0
    for string in DNA:
        n += min([len([0 for j in range(len(Pattern)) if string[i+j]!=Pattern[j]]) for i in range(0, len(string)-len(Pattern)+1)])
        
    return n        

    

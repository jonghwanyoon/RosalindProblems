#
# [BA1G Compute the Hamming Distance Between Two Strings]
# HAMM 과 같음

def BA1G():
    return len([i for i in range(len(s)) if s[i]!=t[i]])

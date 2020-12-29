#
# [BA1F Find a Position in a Genome Minimizing the Skew]
#

def BA1F(DNA):
    score_list = []
    score = 0
    for i in range(len(DNA)):
        score_list.append(score)
        if DNA[i] == 'C':
            score-=1
        elif DNA[i] == 'G':
            score+=1
    s = min(score_list)
    idx = 0
    output = []
    while True:
        try:
            idx = score_list.index(s, idx)
            output.append(idx)
            idx +=1
        except:
            break
    return output
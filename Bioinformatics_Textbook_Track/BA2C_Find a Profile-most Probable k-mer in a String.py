#
# [BA2C Find a Profile-most Probable k-mer in a String]
#
def BA2C(Text : str, k : int, Profile : list) -> str:
    bases = ['A', 'C', 'G', 'T']
    score_dict = {}
    for i in range(0, len(Text) - k + 1):
        subseq = Text[i:i+k]
        score_list = []
        for sub_i in range(k):
            base = subseq[sub_i]
            score = Profile[bases.index(base)][sub_i]
            score_list.append(score)
        score_dict[subseq] = sum(score_list)
    return sorted([[k, score_dict[k]] for k in score_dict], key=lambda x: x[1], reverse=True)[0][0]
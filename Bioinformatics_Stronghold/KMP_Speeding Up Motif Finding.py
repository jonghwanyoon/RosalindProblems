#
# [KMP Speeding Up Motif Finding]
#
# TODO 너무 막코딩인거 같은데.. 결과는 잘 나옴
#

def KMP(s : str) -> list:
    array = []
    index = []
    for i in range(len(s)):
        if i==0:
            array.append(0)
            continue
        max = 0
        del_idx = []
        for j in range(len(index)):
            idx = index[j]
            if s[i] == s[idx]:
                index[j] += 1
                idx +=1 
            else:
                idx = 0
                del_idx.append(j)
            if idx > max:
                max = idx
        for j in del_idx[::-1]:
            del index[j]
        if s[i] == s[0]:
            index.append(1)
            if max == 0:
                max = 1
        array.append(max)    
    return ' '.join(map(str, array))


# from Bio import SeqIO
# parser = SeqIO.parse('input.tsv', format='fasta')
# for record in parser:
#     s = str(record.seq)

# open('output.tsv', 'w').write(KMP(s))
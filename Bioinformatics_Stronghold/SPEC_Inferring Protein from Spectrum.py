
#
# 딱히 알고리즘이랄게 없고, 각 weight 들에서 diff값에 해당하는 weight를 가진 amino acid의 1-letter 들을 반환하면 됨
# 

def SPEC(L):
    w = {}
    for line in open('amino_acid_mass_table.txt'):
        line = line.strip('\n').split('\t')
        if line[0] == 'Name':
            continue
        weight = round(float(line[3]),4)
        aa = line[2]
        w[weight] = aa

    return ''.join([w[round(float(L[i]) - float(L[i-1]), 4)] for i in range(1,len(L))])


# L="""3524.8542
# 3710.9335
# 3841.974
# 3970.0326
# 4057.0646""".split('\n')
# print(SPEC(L))
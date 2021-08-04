



def GET_AA_WEIGHTS():
    w = {}
    for line in open('amino_acid_mass_table.txt'):
        line = line.strip('\n').split('\t')
        if line[0] == 'Name':
            continue
        weight = round(float(line[3]),4)
        aa = line[2]
        w[weight] = aa
    return w

w = GET_AA_WEIGHTS()

def COMB_WEIGHTS(lst, k):
    from itertools import combinations as comb
    out_lst = []
    for i in comb(lst, k):
        weight = sum(i)
        if weight in w:
            out_lst.append(w[weight])
    return out_lst


def FULL(L: list):
    n = int((len(L) -3 )/2)
    weights = list(set([round(float(L[i]) - float(L[i-1]), 4) for i in range(2,len(L))]))

    out_lst = []
    out_lst += COMB_WEIGHTS(weights,2)
    out_lst += COMB_WEIGHTS(weights,1)
    return out_lst
    # excepts = [i for i in weights if i not in w]
    # print(weights)
    # print(excepts)
    # for i in comb(excepts, 2):
    #     weight = sum(i)
    #     if weight in w:
    #         print(w[weight])

    # for i in range(2,len(L)):
    #     print(round(float(L[i]) - float(L[i-1]), 4))

    

L = """1988.21104821
610.391039105
738.485999105
766.492149105
863.544909105
867.528589105
992.587499105
995.623549105
1120.6824591
1124.6661391
1221.7188991
1249.7250491
1377.8200091""".split('\n')

print(''.join(FULL(L)))
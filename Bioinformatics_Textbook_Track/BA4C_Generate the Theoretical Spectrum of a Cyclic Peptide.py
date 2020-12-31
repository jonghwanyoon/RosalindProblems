#
# [BA4C Generate the Theoretical Spectrum of a Cyclic Peptide]
#

def GET_MASS_DICT():
    dic = {}
    for line in open('amino_acid_mass_table.txt'):
        if line.startswith('Name'):
            header = line.strip('\n').split('\t')
            continue
        line=line.strip('\n').split('\t')
        AA  = line[header.index('1-letter code')]
        MASS= int(float(line[header.index('Average Mass')]))
        dic[AA] = MASS
    return dic

def BA4C(Peptide):
    from itertools import combinations as comb
    mass    = GET_MASS_DICT()
    Peptide = list(Peptide)
    n       = len(Peptide)
    Peptide = Peptide+Peptide
    lst = [0]
    for i in range(1, n+1):
        if i == n:
            lst.append(sum([mass[aa] for aa in Peptide[:n]]))
            continue
        for j in range(0, n):
            lst.append(sum([mass[aa] for aa in Peptide[j:j+i]]))
    return sorted(lst)
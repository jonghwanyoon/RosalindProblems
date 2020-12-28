#
# [BA11C Convert a Peptide into a Peptide Vector]
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

def BA11C(lst):
    mass = GET_MASS_DICT()
    output = []
    for i in lst:
        output += ['0' for _ in range(mass[i]-1)] + ['1']
    return ' '.join(output)

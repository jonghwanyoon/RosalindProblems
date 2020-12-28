#
# [BA11C Convert a Peptide Vector into a Peptide]
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
        dic[MASS] = AA
    return dic

def BA11C(vector):
    mass = GET_MASS_DICT()
    output = []
    vector = vector.replace(' ', '').split('1')

    for i in vector[:-1]:
        count = len(i) + 1
        output.append(mass[count])
    return ''.join(output)
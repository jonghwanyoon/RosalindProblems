#
# [BA11B Implement DecodingIdealSpectrum]
# Amino Acid Mass Table이 추가로 필요함.
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

def BA11B(lst):
    from itertools import combinations as cb
    mass = GET_MASS_DICT()
    if 0 not in lst:
        lst.append(0)
    main = []
    for pair in cb(lst, 2):
        m1, m2 = sorted(list(pair))
        diff = m2 - m1
        if diff in mass:
            main.append([m1, m2, mass[diff]])
    main = sorted(main, key=lambda x: x[1])
    main = sorted(main, key=lambda x: x[0])
    output = []
    for i in range(len(main)):
        tmp = [main[i]]
        for j in main[i+1:]:
            if j[0] == tmp[-1][1]:
                tmp.append(j)
        output.append([len(tmp), tmp])
    results = sorted(output, key=lambda x: x[0], reverse=True)
    print(results[1])
    best = results[0]
    aa_output = ''.join([i[2] for i in best[1]])
    return aa_output

data = [int(i) for i in open('input.tsv').readline().split(' ')]
print(BA11B(data))
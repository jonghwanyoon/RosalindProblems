


def MPRT(id_list):
    from urllib import request
    for prot_id in id_list:
        head = ''
        seq = ''
        for line in request.urlopen('https://www.uniprot.org/uniprot/{}.fasta'.format(prot_id)):
            line = line.decode('utf-8').strip('\n')
            if line.startswith('>'):
                head = line
            else:
                seq += line
        ans = []
        i = 0
        while seq.find('N', i) != -1:
            idx = seq.find('N', i)
            if idx+3 > len(seq):
                break
            if seq[idx+2] in ['T','S']:
                ans.append(idx+1)
            i = idx+1

        if len(ans) > 0:
            print(prot_id)
            print(' '.join(map(str,ans)))


A = """P02748_CO9_HUMAN
Q90X23
P05783_K1CR_HUMAN
P72173
P07204_TRBM_HUMAN
P81428_FA10_TROCA
P02186
P98119_URT1_DESRO
P10646_TFPI_HUMAN
A2A2Y4
A9QYR8
O14977
""".split('\n')


MPRT(A)
#
# N-glycosylation motif 찾기.
#
# N{P}[ST]{P} 가 위치한 index 리스트를 return하면 됨 
# {P} = P를 제외한 아무 Amino acid가 올 수 있음
# [ST] = S 혹은 T 만 올 수 있음
#

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
            if idx+3 >= len(seq):
                break
            if seq[idx+2] in ['T','S'] and seq[idx+1] != 'P' and seq[idx+3]!='P' :
                ans.append(idx+1)
            i = idx+1

        if len(ans) > 0:
            print(prot_id)
            print(' '.join(map(str,ans)))
    

# A = """A2Z669
# B5ZC00
# P07204_TRBM_HUMAN
# P20840_SAG1_YEAST""".split('\n')
# MPRT(A)
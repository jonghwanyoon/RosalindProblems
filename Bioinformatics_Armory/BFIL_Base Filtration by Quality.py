
#
# [BFIL	Base Filtration by Quality]
# FASTQ 가 주어지면, q 이하인 quality인 read를 trimming 하면 됨.
#

def BFIL(q, fasta):
    from Bio import SeqIO
    parser = SeqIO.parse(fasta, format='fastq')
    with open('output.tsv', 'w') as w:
        for record in parser:
            idx = []
            score = record.letter_annotations['phred_quality']
            for i in range(len(score)):
                if score[i] < q:
                    idx.append(i)
                else:
                    break
            for i in range(len(score)-1, 0, -1):
                if score[i] < q:
                    idx.append(i)
                else:
                    break

            w.write('@' + record.id + '\n')
            w.write(''.join([str(record.seq)[i] for i in range(len(record.seq)) if i not in idx])+'\n')
            w.write('+\n')
            w.write(''.join([chr(score[i]+33) for i in range(len(score)) if i not in idx])+'\n')

#
# FILT	Read Filtration by Quality
# quality threshold 'q', base 퍼센트 'p', fastq 포맷이 주어지고,
# quality가 q 이상인 base가 p % 이상인 read가 몇개인지 나타내면 됨.
#
# 참고) ascii to int : ord('F') 여기서 나타나는 거에 -33을 해주면 quality임.
#


def FILT(q, p, fastq):
    from Bio import SeqIO
    parser = SeqIO.parse(fastq, format='fastq')
    c = 0
    for record in parser:
        score=record.letter_annotations["phred_quality"]
        idx = (len([None for i in score if i >= q])/len(score))*100
        if idx >= p:
            c+=1
    return c

#
# [BPHR	Base Quality Distribution]
# quality threshold 'q', fastq 포맷이 주어지고,
# 각 position의 mean base quality가 q 이하인게 몇 개인지 나타내면 됨.
#


def FILT(q, fastq):
    from Bio import SeqIO
    parser = SeqIO.parse(fastq, format='fastq')
    main =[]
    for record in parser:
        score=record.letter_annotations["phred_quality"]
        main.append(score)
    
    return len([None for i in range(len(main[0])) if sum([s_set[i] for s_set in main])/len(main) < q ])

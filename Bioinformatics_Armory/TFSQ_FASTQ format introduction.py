
#
# Fastq가 주어지면 Fasta format으로 반환하는 문제.
#

def TFSQ(fastq):
    from Bio import SeqIO
    parser = SeqIO.parse(fastq, format='fastq')
    for record in parser:
        print('>'+record.id)
        print(str(record.seq))


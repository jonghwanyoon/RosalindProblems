#
# [GRPH Overlab Graphs]
#

def GRPH(fasta):
    from Bio import SeqIO
    parser = SeqIO.parse(fasta, format='fasta')
    dic = {}
    k = 3
    prefix_set = {}
    suffix_set = {}
    for record in parser:
        id = record.id
        seq = record.seq
        prefix = seq[:k]
        suffix = seq[-k:]
        if prefix not in prefix_set:
            prefix_set[prefix] = []
        prefix_set[prefix].append(id)
        if suffix not in suffix_set:
            suffix_set[suffix] = []
        suffix_set[suffix].append(id)
    
    main = []
    for k in suffix_set:
        if k not in prefix_set:
            continue
        id1 = suffix_set[k]
        id2 = prefix_set[k]

        for node1 in id1:
            for node2 in id2:
                if node1 == node2:
                    continue
                main.append([node1, node2])
    return main

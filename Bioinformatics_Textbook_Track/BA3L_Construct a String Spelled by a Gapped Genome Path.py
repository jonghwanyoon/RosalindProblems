#
# [BA3L Construct a String Spelled by a Gapped Genome Path]
#
def BA3L(k : int, d : int, Patterns : list):
    DNA = Patterns[0].split('|')
    for i in range(1, len(Patterns)):
        prefix, suffix = Patterns[i].split('|')
        DNA[0] += prefix[-1]
        DNA[1] += suffix[-1]
    idx = DNA[0].find(DNA[1][:d])
    sequence = DNA[0][:idx] + DNA[1]
    return sequence

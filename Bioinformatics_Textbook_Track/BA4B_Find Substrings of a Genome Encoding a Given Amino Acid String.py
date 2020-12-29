#
# [BA4B Find Substrings of a Genome Encoding a Given Amino Acid String]
#
def BA4B(Pattern, Peptide):
    from Bio.Seq import Seq
    k = len(Peptide)*3
    out = []
    for i in range(len(Pattern)-k +1):
        seq = Seq(Pattern[i:i+k])
        aa  = seq.translate()
        revc = seq.reverse_complement()
        revc_aa = revc.translate()
        if aa == Peptide or revc_aa == Peptide:
            out.append(str(seq))
    return out
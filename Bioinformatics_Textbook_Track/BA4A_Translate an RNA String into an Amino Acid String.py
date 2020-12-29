#
# [BA4A Translate an RNA String into an Amino Acid String]
#

def BA4A(Pattern):
    from Bio.Seq import Seq
    return Seq(Pattern).translate()



def PROT(s):
    from Bio import Seq
    return Seq.translate(s)
    
# print(PROT('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))
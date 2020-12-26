#
# [BA3B Reconstruct a String from its Genome Path]
#

def BA3B(DNA_list):
    return DNA_list[0] + ''.join([DNA_list[i][-1] for i in range(1, len(DNA_list))])

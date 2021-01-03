#
# [BA3C Construct the Overlap Graph of a Collection of k-mers]
#

def BA3C(Patterns : list):
    prefix_dict = {}
    suffix_dict = {}
    for p in Patterns:
        prefix = p[:-1]
        suffix = p[1:]
        if prefix not in prefix_dict:
            prefix_dict[prefix] =[]
        prefix_dict[prefix].append(p)

        if suffix not in suffix_dict:
            suffix_dict[suffix] =[]
        suffix_dict[suffix].append(p)
    out = []
    for k in suffix_dict:
        if k not in prefix_dict:
            continue
        for suffix in suffix_dict[k]:
            for prefix in prefix_dict[k]:
                out.append('{} -> {}'.format(suffix, prefix))
    return sorted(out)
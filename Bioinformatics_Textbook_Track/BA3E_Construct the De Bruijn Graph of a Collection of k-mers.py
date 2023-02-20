#
# [BA3E Construct the De Bruijn Graph of a Collection of k-mers]
#
# 간단한 방법은 dictionary를 이용하면 BA3E로 표현 가능하다.
#


from collections import defaultdict

def BA3E(Patterns):
    dic=defaultdict(list)
    for p in Patterns:
        dic[p[:-1]].append(p[1:])
    for k in sorted(list(dic.keys())):
        print('{} -> {}'.format(k, ','.join(sorted(dic[k]))))



class Node:
    def __init__(self, value):
        self.value = value
        self.child = []

    def addChild(self, node):
        self.child.append(node)

    def extendChilds(self, node_list):
        self.child.extend(node_list)


def BA3E_2(Patterns):
    # Composition Graph
    pool = []
    for p in Patterns:
        prefix = Node(p[:-1])
        suffix = Node(p[1:])
        prefix.addChild(suffix)
        pool.append(prefix)
    
    # Path Graph
    dic = {}
    for node in pool:
        prefix = node.value
        if prefix not in dic:
            dic[prefix] = node
        else:
            dic[prefix].extendChilds(node.child)

    for kmer, node in dic.items():
        prefix = node.value # equal with kmer
        suffix_list = [child.value for child in node.child]
        print(prefix + " -> " + ",".join(suffix_list) + "\n")
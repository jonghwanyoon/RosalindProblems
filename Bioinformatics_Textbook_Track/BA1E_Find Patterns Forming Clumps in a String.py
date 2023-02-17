"""
clump를 찾는 문제

길이 L 내에 k-mer가 t번 나타나는 경우, 해당 k-mer는 clump를 구성한다고 할 수 있다.
해당되는 k-mer를 모두 반환하면 된다.

두 가지 해결 방안이 있다. -> BA1E, BA1E_2

BA1E의 아래의 코드의 시간복잡도는 O((|G| - L)*(L - k)) 이다.
윈도우가 이동될 때마다 길이 L의 sub genome 배열에서 빈번한 Kmer를 찾기 때문에 비효율적이다.

윈도우가 이동될 때마다, 대부분의 배열은 바뀌지 않는다는 것을 감안하면, window의 양 끝 kmer만 확인하면 된다.
따라서, BA1E_2의 함수로 구현할 수 있다. 시간복잡도는 O(|G| - k) 정도로 보인다.

두 함수의 속도 차이는 다음과 같다.
BA1E = 602 µs ± 4.3 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
BA1E_2 = 40.7 µs ± 852 ns per loop (mean ± std. dev. of 7 runs, 10000 loops each)
"""

from typing import List, Dict
from collections import defaultdict

def KmerFrequency(s: str, k: int) -> dict:
    count = defaultdict(int)
    for i in range(len(s) - k + 1): # O(L - k + 1)
        count[s[i:i+k]] += 1
    return count

def BA1E(G: str, k: int, L: int, t: int) -> set:
    result = set()
    for i in range(len(G) - L + 1): # O(len(G) - L + 1)
        s = G[i:i+L]
        count_dict = KmerFrequency(s, k)
        kmer_list = [key for key,val in count_dict.items() if val >= t]
        result.update(kmer_list)
    return result

def BA1E_2(G: str, k: int, L: int, t: int) -> set:
    result = set()
    s = G[:L]
    count_dict = KmerFrequency(s, k) # O(L - k + 1)
    kmer_list = [key for key,val in count_dict.items() if val >= t]
    result.update(kmer_list)
    for i in range(1, len(G) - L + 1): # O(len(G) - L )
        # Check the both side's kmer.
        before_kmer = G[i-1:i+k-1]
        next_kmer = G[i+L-k:i+L]
        count_dict[before_kmer] -= 1
        count_dict[next_kmer] += 1
        if count_dict[next_kmer] >= t:
            result.add(next_kmer)
    return result

G = "CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC"
k = 5
L = 75
t = 4

print(" ".join(BA1E_2(G, k, L, t)))
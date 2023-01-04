"""
https://rosalind.info/problems/seto/

int n과 두 개의 set이 주어졌을 때, 아래 6가지를 출력하라.

- A와 B의 합집합
- A와 B의 교집합
- A - B
- B - A
- A의 여집합
- B의 여집합
"""

def SETO(n: int, A: set, B: set):
    whole = set(range(1, n+1))
    union = A | B
    intersect = A & B
    diff_A = A - B
    diff_B = B - A
    comp_A = whole - A
    comp_B = whole - B
    return [union, intersect, diff_A, diff_B, comp_A, comp_B]
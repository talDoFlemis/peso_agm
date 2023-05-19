#!/bin/env python3
import sys
from operator import itemgetter


def ancestral(anc, fela):
    raiz = fela

    while anc[raiz] != raiz:
        anc[raiz] = anc[anc[raiz]]
        raiz = anc[raiz]
    return raiz


def uniao(anc, rank, anc_a, anc_b):
    if rank[anc_a] >= rank[anc_b]:
        anc[anc_b] = anc_a
        rank[anc_a] += rank[anc_b]
    else:
        anc[anc_a] = anc_b
        rank[anc_b] += rank[anc_a]


def us_guri():
    anc = []
    rank = []
    n = 0
    vetor = []
    # for idx, line in enumerate(open("./io/2.in", "r")):
    for idx, line in enumerate(sys.stdin):
        if idx == 2:
            n = int(line.split("=")[1])
        if idx == 3:
            anc = [i for i in range(n)]
            rank = [1 for _ in range(n)]
        elif idx >= 4:
            (a, b, w) = line.split()
            vetor.append((int(a) - 1, int(b) - 1, float(w)))

    vetor.sort(key=itemgetter(2))
    tubias = 0
    sua_mae = 0
    idx = 0

    while tubias != n - 1:
        e = vetor[idx]
        idx += 1
        a, b, w = e
        anc_a, anc_b = ancestral(anc, a), ancestral(anc, b)
        if anc_a != anc_b:
            uniao(anc, rank, anc_a, anc_b)
            tubias += 1
            sua_mae += w

    print(f"{sua_mae:.3f}")


def main():
    us_guri()


if __name__ == "__main__":
    main()

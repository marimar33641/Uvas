#Codigo basado en la estructura de textsegmentation visto en clase
from sys import stdin
import sys
sys.setrecursionlimit(1000000)
sols = []

def solve( n, sequencesTotal, sequenceLine, D ):
    global sols
    sols.append(sequenceLine)
    if sequencesTotal == K:
        sols.append(sequenceLine)
    else:
        while n < N:
            for i in D:
                solve( n + 1, sequencesTotal + 1, sequenceLine[ :n ] + i + sequenceLine[ n + 1: ], D )
            n += 1

def main():
    global K, N, sols
    T = int(stdin.readline())
    D = ['A', 'G', 'C', 'T' ]
    for _ in range(T):
        sequenceLine = []
        N, K =  map(int,stdin.readline().split())
        sequenceLine = stdin.readline().strip()
        sols = []
        solve( 0, 0, sequenceLine, D )
        sols = sorted(set(sols))
        print(len(sols))
        for k in sols:
            print(k)
main()
#A - Philip J. Fry Problem
#Codigo clase 2 marzo- Camilo Rocha
from sys import stdin
def phi( T, E ):
    N, SE = len(T), sum(E)
    tab = [ [ 0 for _ in range((SE<<1)+1) ] for _ in range(2) ]
    n, e, curr, prev = N-1, 0, 0, 1
    while n!= -1:
        if e == SE+1: 
            n,e,curr,prev = n-1,0,1-curr, 1-prev
        else:
            if e == 0: tab[curr][e] = T[n]+tab[prev][E[n]]
            else: tab[curr][e] = min(T[n]+tab[prev][e+E[n]],(T[n]>>1)+tab[prev][e+E[n]-1])
            e+=1
    return tab[prev][0]

def main():
    T = [24,10]
    E = [1, 0]
    
    c = int(stdin.readline())
    while c != 0:
        T1 = []
        E1 = []
        for _ in range(c):
            vals = stdin.readline().split()
            T1.append(int(vals[0]))
            E1.append(int(vals[1]))
            #print(vals)
            #print(T1, E1)
        print(phi(T1, E1))
        c = int(stdin.readline())
    
main()

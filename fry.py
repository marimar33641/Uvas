#Se hizo por tabulación by Camilo Rocha
#Lo implemente con memorización de acuerdo a la clase 2 de marzo con Camilo Rocha

from sys import stdin
def phi(n, e, T, E, mem ):
    N, ans = len(T), None
    if (n, e) in mem: ans = mem[(n, e)]
    else:
        if n == N: ans = 0
        else:
            if n != N and e == 0: 
                ans = T[n]+ phi( n+1, e+E[n], T, E, mem )
            else: 
                ans =  min(T[n]+ phi( n+1, e+E[n], T, E, mem ),(T[n]>>1)+ phi( n+1, e+E[n]-1, T, E, mem ) )
            mem[(n, e)] = ans
    return ans
def main():
    c = int(stdin.readline())
    while c != 0:
        T1 = []
        E1 = []
        mem = {}
        for _ in range(c):
            vals = stdin.readline().split()
            T1.append(int(vals[0]))
            E1.append(int(vals[1]))
        print(phi(0, 0, T1, E1, mem))
        c = int(stdin.readline())   
main()
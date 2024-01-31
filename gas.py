#Codigo tomado de Rocha en el curso de ADA- es decir, la funcion mic_wf se tomo del material de estudio de los cursos de ADA. 2019-1
#Sesion 13-14: https://www.camilorocha.info/teaching/ada/2019-1
#Link: https://bitbucket.org/snippets/hquilo/z6KbA

from sys import stdin

def mic_wf(L, H, a):
    a.sort()
    ans,low, n, ok, N = 0,L, 0, True, len(a)
    while ok and low<H and n!=N:
        ok = a[n][0]<=low
        best, n = n, n + 1
        while ok and n!=N and a[n][0]<=low:
            if a[n][1]>a[best][1]:
                best = n
            n += 1
        ans += 1
        low = a[best][1]
    ok = ok and low>=H
    if ok == False:
        ans = -1
    return ans

def main():
    L, G = map(int, stdin.readline().split())
    while (L != 0 and G != 0):
        gasS = []
        for i in range(G):
            x, r = map(int, stdin.readline().split())
            gasS.append((x-r,x+r))
        ans = mic_wf(0, L, gasS)
        if (ans == -1):
            print(ans)
        else:
            print(G-ans)
        L, G = map(int, stdin.readline().split())	

main()
#Codigo tomado de la clase de Carlos Ramirez, en donde resolvio el problema de scores. La funcion solve esta tal cual y en check tambien, pero pues se ajusto a la cantidad de urnas; Y en scores era el numero de scores.
from sys import stdin

def check( A, mid, B  ):
    ac = 0
    for v in A:
        if( v % mid ) == 0: ac += ( v // mid )
        else: ac += ( v // mid ) + 1
    ans = ac <= B
    return ans

def solve( A, B ):
    l, r = 0, max(A)
    while r-l != 1:
        mid = l + ((r-l)//2)
        if check( A, mid, B ): r = mid
        else: l = mid
    return r

def main():
    N, B = list(map(int, stdin.readline().split()))
    while N != -1 and B != -1:
        A = [ int(stdin.readline()) for _ in range(N) ]
        stdin.readline()
        ans = solve( A, B )
        print(ans)
        N, B = list(map(int, stdin.readline().split()))
main()

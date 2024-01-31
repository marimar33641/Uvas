from sys import stdin
def phi(B, T1, T2, A, n, x, mem):
    N, ans = len(A), None
    if(n,x) in mem: ans=mem[ (n,x) ]
    else:
        if( n == N - 1 and x == -1 ): 
            ans = T1
        elif( n == N - 1 ): 
            ans = 0
        elif( x == 0 ):
            ans = phi(B, T1, T2, A, n + 1, max(x - B[n], 0), mem)
        else: 
            ans = min(phi(B, T1, T2, A, n + 1, max(T1 - B[ n ],-1), mem) + T1, phi(B, T1, T2, A, n + 1, max(T2 - B[ n ], -1), mem) + T2, phi(B, T1, T2, A, n + 1, max(x - B[ n ], 0), mem))
        mem[ (n,x) ] = ans
    return ans

def main():
    c = stdin.readline().split()
    while c != []:
        N, C, T1, T2 = int(c[0]), int(c[1]), int(c[2]), int(c[3])
        #print("a: ", N, C, T1, T2)
        distances = list(map(int, input().split()))
        distances2 = []
        for i in range( N - 1):
            distances2.append( distances[i+1]-distances[i] )
        #print(distances2)
        print(phi(distances2,T1, T2, distances, 0, -1, {} ))
        c = stdin.readline().split()
main()
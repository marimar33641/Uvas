"""
Maria Del Mar Villaquiran Davila
22 de septiembre 2021
Codigo: Basado con los conceptos vistos en clase y los codigos de bfs que el profesor a subido
"""
from sys import stdin
from collections import deque
MAX = 30
visitados = [False for _ in range(MAX)]
adj = [[] for _ in range(MAX)]
p = [0 for _ in range(MAX)]

def bfsAux( v ):
    cola = deque()
    cola.append( v )
    visitados[ v ] = True
    while( len(cola) != 0 ):
        u = cola.popleft()
        for i in range( len(adj[ u ]) ):
            w = adj[ u ][ i ]
            if not visitados[ w ]:
                cola.append( w )
                visitados[ w ] = True
                p[ w ] = p[ u ] + 1

def bfs( t, u, v, M ):
    for i in range( M ):
        visitados[ i ] = False
        p[ i ] = 0
    for i in range( M ):
        if not visitados[ i ]:
            bfsAux( u )
    if( p[ v ] ):
        print("$%d" % ( p[ v ] * t * 100 ))
    else:
        print( "NO SHIPMENT POSSIBLE" )   

def main():
    global adj
    sets = int(stdin.readline())
    print("SHIPPING ROUTES OUTPUT")
    cases = 1
    for i in range(sets):
        vals = {}
        M, N, P = list(map(int, stdin.readline().split()))
        nombreCodigo =list(map(str, stdin.readline().split()))
        for j in range(M):
            vals[ nombreCodigo[ j ] ] = j
        for j in range( N ):
            inicio, final = list(map(str, stdin.readline().split()))
            u =  vals[ inicio ]
            v = vals[ final ]
            adj[ u ].append( v )
            adj[ v ].append( u )
        print("\nDATA SET  %d\n" % ( cases ))
        for j in range( P ):
            tamanioEnvio, almacen1, almacen2 = list(map(str, stdin.readline().split()))
            u = vals[ almacen1 ]
            v = vals[ almacen2 ]
            bfs( int(tamanioEnvio), u, v, M )
        adj = [[] for _ in range(MAX)]
        cases += 1
    print("\nEND OF OUTPUT")
main()
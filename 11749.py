"""
Maria Del Mar Villaquiran Davila
11 de octubre
"""

from sys import stdin
MAX = 505
adj = [[] for i in range( MAX )]
visitados = [0 for i in range( MAX )]
ciudades, caminosM, n = 1, 0, 0
#DFS con solo un contador de ciudades (ligera modificacion de un dfs)

def dfsAux( v ):
    global ciudades
    visitados[ v ] = 1
    for u in adj[ v ]:
        if visitados[ u ] == 0:
            dfsAux( u )
            ciudades += 1
    
def dfs( ):
    global ciudades, caminosM, n
    for i in range( n + 1 ):
        visitados[ i ] = 0
    for i in range(n):
        if visitados[ i ] == 0:
            ciudades = 1
            dfsAux( i )
            caminosM = max(caminosM, ciudades)
           
def main():
    global n, caminosM
    n, m = list(map(int, stdin.readline().split()))
    while( n != 0 and m != 0 ):
        vals = []
        maxPPA = float('-inf')
        for i in range(MAX):
            adj[i].clear()
        for i in range(m):
            u, v, PPA = list(map(int, stdin.readline().split()))
            vals.append( [ u,v, PPA ] )
            maxPPA = max( maxPPA, PPA )
        for i in range(m):
            if( vals[i][2] == maxPPA ): #Para no trabajar con todo el grafo, se hace que solo se trabaje con los nodos con peso maximo, de resto es un dfs facil.
                adj[vals[i][0]].append(vals[i][1])
                adj[vals[i][1]].append(vals[i][0])
        dfs()
        print( caminosM )
        caminosM = 0
        n, m = list(map(int, stdin.readline().split()))

main()
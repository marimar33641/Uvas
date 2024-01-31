"""
Maria del mar Villaquiran Davila
23 de septiembre 2021
"""

from sys import stdin
from collections import deque
MAX = 1000000
adj = [[] for i in range( MAX )]
visitados = [0 for i in range( MAX )]
oleoductos = 0
conex = 0
ciudades = 0
topo = deque()

#Dfs para obtener el orden topologico del grado

def dfsAux( v ):
    global topo
    visitados[ v ] = 1
    for u in adj[ v ]:
        if visitados[ u ] == 0:
            dfsAux( u )
    topo.appendleft( v )

def dfs( ):
    for i in range(oleoductos):
        visitados[ i ] = 0
    for i in range(oleoductos):
        if visitados[ i ] == 0:
            dfsAux( i )

#Dfs con el orden topologico

def dfsTopoAux( v ):
    global topo, conex
    visitados[ v ] = 1
    for u in range( len(topo) ):
        w = topo[ u ]
        if( visitados[ w ] == 0 ):
            conex += 1
            dfsTopoAux( w )

def dfsTopo():
    for i in range(ciudades):
        visitados[ i ] = 0
    for i in range(ciudades):
        if visitados[ i ] == 0:
            dfsTopoAux( i )

def main():
    global oleoductos, topo, conex, ciudades
    ciudades, oleoductos = list(map(int, stdin.readline().split()))
    while( ciudades != "" and oleoductos != "" ):
        adj = [[] for i in range( MAX )]
        conex = 0
        for i in range( oleoductos ):
            u, v = list(map(int, stdin.readline().split()))
            adj[ u ].append( v )
        dfs()
        #print("topo: ", *topo)
        dfsTopo()  
        #print("conex: ", conex )
        print( conex ) 
        topo = deque()
        ciudades, oleoductos = list(map(int, stdin.readline().split()))
main()
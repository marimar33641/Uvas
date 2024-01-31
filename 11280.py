"""
Maria Del Mar Villaquiran Davila
21 de Noviembre 2021
"""
from collections import deque
from sys import stdin

G = {}
d = {}
N = int()
# Complejidad Temporal = O(n * m)
# Complejidad Espacial = O(n * n)
def bellmanFordOpt(city):
    global d, p, N
    n, ans = len(G), True
    #d = [[float('inf') for _ in range(n)] for _ in range(n)]
    d = {_ : float('inf') for _ in city }
    p = [-1 for _ in range(n)]
    d["Calgary"] = 0
    l = {}
    for i in range(n):
        for u in city:
            for v, w in G[u]:
                if d[v] > d[u] + w :
                    d[v] = d[u] + w
        if d["Fredericton"] == float('inf'):
            l[i] = [ False ]
        else:
            l[i] = [True, str(d["Fredericton"])] 
    return l
    
def main():
    global N
    cases = int(stdin.readline())
    escenario = 1
    f = 0
    for i in range( cases ):
        f +=1
        if stdin.readline() != "": #Espacio en la segunda linea
            N = int(stdin.readline())
            city = []
            for j in range( N ):
                cities = stdin.readline().strip()
                G[cities] = []
                city.append(cities)
            M = int(stdin.readline())
            for j in range( M ):
                vuelos = list(map(str, stdin.readline().split()))
                ciudadSalida = vuelos[0]
                ciudadDestino = vuelos[1]
                costo = int(vuelos[2])
                G[ciudadSalida].append((ciudadDestino, costo))
            stopovers = []
            l = list(map(int, stdin.readline().split()))
            for j in range( 1, l[0] + 1 ):
                stopovers.append(l[j])
            city.reverse()
            print("Scenario #%d" % escenario)
            x = bellmanFordOpt(city)
            #print(x)
            #print("stop: ", stopovers)
            if d["Fredericton"] != float('inf'):
                for i in stopovers:
                    if i > len(G):
                        x[i] = [True, str(d["Fredericton"])]
            for j in stopovers:
                if x[j][0] == False:
                    print("No satisfactory flights")
                else:
                    print("Total cost of flight(s) is $" + x[j][1])
            if f != cases:
                print()
            escenario +=1
main()
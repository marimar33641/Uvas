"""
Maria Del Mar Villaquiran Davila
11 de octubre
"""
from sys import stdin
MAX = 50
adj = [[] for i in range(MAX)]
visitado, low = [-1 for i in range(MAX)], [-1 for i in range(MAX)]
enPila = [False for i in range(MAX)] 
n, t, numSCC = int(), 0, 0
sccNodos, pila = [], []
vals2 = []
#Basado en la implementacion de tarjan del code del profesor, para componentes fuertemente conexos
def tarjanAux(v):
    global t, numSCC
    t += 1
    visitado[v], low[v] = t, t
    pila.append(v)
    enPila[v] = True
    for i in range(len(adj[v])):
        w = adj[v][i]
        if visitado[w] == -1:
            tarjanAux(w)
            low[v] = min(low[v], low[w])
        elif enPila[w]:
            low[v] = min(low[v], visitado[w])

    if low[v] == visitado[v]:
        sccNodos.append([])
        numSCC += 1
        while pila[-1] != v:
            a = pila.pop()
            enPila[a] = False
            sccNodos[numSCC - 1].append(a)

        a = pila.pop()
        enPila[a] = False
        sccNodos[numSCC - 1].append(a)

def tarjan():
    global vals2
    for i in range(len(vals2)):
        low[ i ], visitado[ i ], enPila[ i ] = -1, -1, False
    for i in range(len(vals2)):
        if visitado[i] == -1:
            tarjanAux(i)

def main():
    global n, vals2, numSCC
    n = int( stdin.readline())
    while n != 0:
        vals = []
        vals3 = []
        c = 0
        for i in range(n):
            l = list(map(str, stdin.readline().split()))
            for j in l:
                if j not in vals: 
                    vals.append(j)
                    vals2.append(c)
                    c +=1
            for j in l:
                if j != l[-1]:
                    adj[vals.index(l[-1])].append(vals.index(j))
        tarjan()
        for i in sccNodos:
            vals4 = []
            for j in i:
                vals4.append( vals[ j ] )
                vals4.sort()
            vals3.append(vals4)
        vals3.sort()
        for i in vals3:
            for j in i:
                if j  != i[-1]:
                    print(j, end= " ") 
                else:
                    print(j, end="")
            print("")       
        n = int( stdin.readline())
        vals2, t, numSCC = [], 0, 0
        sccNodos.clear()
        for i in range(MAX):
            adj[i].clear()
        if n != 0:
            print()
        
main()
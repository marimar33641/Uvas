/*
Maria del mar Villaquiran Davila
12 de octubre
*/

#include <vector>
#include <stack>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <cstdio>
#include <cstring>

using namespace std;

int n, t;
vector<vector<int> > adj(10005);
int visitado[10005];
int low[10005];
int padre[10005];
int numHijos[10005];
//Code de la implementacion de tarjanAp del profesor, con una ligera modificacion a la hora de sumar los hijos.  

void apAux(int);

void ap(){
    int i;
    for(i = 0; i < n; i++)
        low[i] = visitado[i] = padre[i] =-1;
    for(i = 0; i < n; i++)
        if(visitado[i] == -1)
        apAux(i);
}

void apAux(int v){
    int w;
    visitado[v] = low[v] = ++t;
    numHijos[ v ] = 1;
    for(int i = 0; i < adj[v].size(); i++){
        w = adj[v][i];
        if(visitado[w] == -1){
            padre[w] = v;
            apAux(w);
            low[v] = min(low[v], low[w]);
            //verificar si es un punto de articulacion
            if( low[w] >= visitado[v]){
                numHijos[v]++;
            }
        }
        else if(w != padre[v]){
            low[v] = min(low[v], visitado[w]);
        }
    }
    //if(padre[v] == -1 && numHijos > 1)
        //apNodos.insert(v);
}

bool comparador(pair<int, int> A, pair<int, int> B){ //comparador para poder colocarlo como lo decia el problema, es decir, primero ordenarse por el valor de la paloma en orden descendente y luego por el numero de estacion de entren de orden ascendente
	if( A.second == B.second ){
        return A.first < B.first;
    }
    else{
        return A.second > B.second;
    }
}

int main(){
    int m, i, u, v;
    while( cin >> n >> m &&  n != 0 && m != 0 ){
        for( i = 0; i < 10005; i++ ){
            adj[i].clear();
        }
        while( cin >> u >> v && u+v != -2 ){
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        ap();
        vector< pair <int, int> > apNodos;
        numHijos[0]--; // Inicializo las estaciones con minimo un hijo. Si no hago esto significa que empiezo desde la estacion 1, pero necesito que comience desde la estacion 0.
        for( i = 0; i < n; i++ ){
            //printf("%d, ", numHijos[i]);
            apNodos.push_back(pair <int, int>( i, numHijos[i] )); 
        }
        sort( apNodos.begin(), apNodos.end(), comparador ); //el sort para organizarlo con el comparador y de resto solo es recorrerlo e ir imprimiendo
        int j = 0;
        for( vector< pair <int, int> >::iterator it = apNodos.begin(); it != apNodos.end() && j < m ; ++it ){
            j++;
            printf("%d %d\n", it->first, it->second );
        }
        apNodos.clear();
        printf("\n");
    }
}
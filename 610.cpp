/*
Maria Del Mar Villaquiran Davila
11 de octubre
*/

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

int n, numSCC, t;
vector<vector<int> > adj(1005);
int visitado[1005];
int low[1005];
bool enPila[1005];
stack<int> pila;
vector<vector<int> > sccNodos;

//Codigo basado en la implementacion del algoritmo de tarjan del profesor, para componentes fuertemente conexos (que es lo que nos pide el problema)

void tarjanAux(int);

void tarjan(){
    int i;
    for(i = 0; i < n; i++){
        low[i] = visitado[i] = -1;
        enPila[i] = false;
    }
    for(i = 0; i < n; i++)
        if(visitado[i] == -1)
            tarjanAux(i);
}

void tarjanAux(int v){
    int w;
    visitado[ v ] = low[ v ] = ++t;
    pila.push( v );
    enPila[v] = true;
    for(int i = 0; i < adj[v].size(); i++){
        w = adj[ v ][ i ];
        if(visitado[ w ] == -1){
            tarjanAux( w );
            low[v] = min(low[ v ], low[ w ]);
        }
        else if(enPila[w])
            low[v] = min(low[ v ], visitado[ w ]);
    }
    if(low[v] == visitado[ v ]){
        //cout << "SCC con indice " << low[v] << ": ";
        //sccNodos.push_back(vector<int>());
        //cout << pila.top() << " ";
        numSCC++;
        while(pila.top() != v){
            enPila[pila.top()] = false;
            pila.pop();
        }
        //cout << pila.top() << endl;
        //enPila[pila.top()] = false;
        //sccNodos[numSCC - 1].push_back(pila.top());
        //pila.pop();
    }
}
int main(){
    int n, m, i, j, cases = 1, u, v;
    cin >> n >> m;
    while( n != 0 && m != 0 ){
        for( i = 0; i < m; i++ ){
            cin >> u >> v;
        }
        for( i = 0; i < m; i++ ){
           if( !visitado[ i ] ){
               tarjan();
           }
        }
        printf("%d\n\n", cases);
        cases++;
        for( i = 0; i < n; i++ ){
            for( j = 0; j < m; j++ ){
                if( !visitado[i] ){
                    printf("%d %d\n", i, j);
                }
            }
        }        
        printf( "#\n" );    
        cin >> n >> m;  
    }
    return 0;
}
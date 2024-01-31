/*
Maria Del Mar Villaquiran Davila
20 de noviembre 2021
*/

#include <climits>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;
int n;
vector<vector<pair<int, int> > > adj(50000);
vector<int> p(50000);
vector<pair<int, int> > d(50000);

void inicializar(int s){
  for(int i = 0; i < n; ++i){
    d[i].first = INT_MAX;
    d[i].second = INT_MAX;
    p[i] = -1;
  }
}

void dijkstra(int s){
    int i, j, k, u, v, peso, costo;
    priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>> > cola;
    inicializar(s);
    cola.push(make_pair(0, s));
    while(!cola.empty()){
        costo = cola.top().first;
        u = cola.top().second;
        cola.pop();
        if(costo != d[u].first){
            for(j = 0; j < adj[u].size(); ++j){
            	v = adj[u][j].first;
            	peso = adj[u][j].second;
                if( costo + peso < d[v].second ){
                    cola.push(make_pair(costo+peso ,v));
                }
            }
            if( costo < d[u].first ){
                d[u].first = costo;
            }
            else if( costo < d[u].second ){
                d[u].second = costo;
            }
        }
    }
}

int main(){
    int r, i, q, set = 1, j, u, v;
    while( scanf("%d %d", &n, &r) == 2 ){
        for(i = 0; i < n; i++){
            adj[i].clear();
        }
        for(i = 0; i < r; i++){
            int aux1, aux2, peso;
            cin >> aux1 >> aux2 >> peso;
            adj[aux1].push_back(make_pair(aux2, peso));
            adj[aux2].push_back(make_pair(aux1, peso));
        }
        printf("Set #%d\n", set);
        cin >> q;
        for( j = 0; j < q; j++ ){
            cin >> u >> v;
            dijkstra(u);
            //cout << d[j].first << "         " << d[j].second << endl;
            if (d[v].second == INT_MAX){
                printf("?\n");
            }
            else{
                printf("%d\n", d[v].second);
            }
        }
        set++;
    }
    return 0;
}
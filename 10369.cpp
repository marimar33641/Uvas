/*
Maria Del Mar Villaquiran Davila
20 de noviembre 2021
*/
using namespace std;

#include <climits>
#include <vector>
#include <algorithm>
#include <iostream>
#include <math.h>

using namespace std;

//operaciones disjoint set union
//**************
int padre[50000], rango[50000];

void makeSet(int v){
  padre[v] = v;
  rango[v] = 0;
}

int findSet(int v){
  if(v == padre[v])
    return v;
  else{
    padre[v] = findSet(padre[v]);
    return padre[v];
  }
}

void unionSet(int u, int v){
  u = findSet(u);
  v = findSet(v);

  if(u != v){
    if(rango[u] < rango[v])
      swap(u, v);
    
    padre[v] = u;
    if(rango[u] == rango[v])
      rango[u]++;
  }
}
//**************

struct Arista{
  int u, v;
  double peso;

  Arista(){}

  Arista(int x, int y, double p){
    u = x;
    v = y;
    peso = p;
  }

  bool operator<(Arista& a){
    return peso < a.peso;
  }
};

int S,P;
double total;
vector<Arista> aristas;
vector<Arista> mst;

void kruskal(){
  int i, u, v, p2;
  int c = 0;
  double maxTree = -1, p1 = 0;
  for(i = 0; i < P; ++i)
      makeSet(i);
  sort(aristas.begin(), aristas.end());
  for(vector<Arista>::iterator it = aristas.begin(); it != aristas.end(); ++it){
      u = it->u;
      v = it->v;
      p1 = it->peso;
      
      if(findSet(u) != findSet(v)){
          mst.push_back(*it);
          c++;
          total += it->peso;
          unionSet(u, v);
          //printf("p1: %f\n", p1);
          maxTree = max(maxTree, p1 );
          if( c == P - S ){
              printf("%.2f\n", maxTree);
          }
      }
      it-> u = 0;
      it-> v = 0;
      it-> peso = 0;
  }
}

int main(){
    int cases, i, j, aux1, aux2, k;
    double u,v,p;
    cin >> cases;
    for( i = 0; i < cases; ++i ){
        cin >> S >> P;
        vector<int> x(P,0);
        vector<int> y(P,0);
        for( j = 0; j < P; j++ ){
            scanf("%d%d", &x[j],&y[j]);
            //cin >> aux1 >> aux2;
        }
        for( j = 0; j < P - 1; j++ ){
            for( k = j+1; k < P; k++ ){
                v = y[ j ] - y[ k ]; 
                u = x[ j ] - x[ k ];
                p = sqrt((pow(u,2))+(pow(v,2)));
                aristas.push_back(Arista(j, k, p));
            }
        }
        kruskal();
        //printf("%.2f", kruskal());
    }
}
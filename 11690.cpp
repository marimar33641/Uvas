#include <iostream>
using namespace std;
int amigos[ 10005 ];
int dinero1[ 10005 ];
int dinero2[ 10005 ];

int encontrarAmigo( int v ){
    if( amigos[ v ] != v ) return amigos[ v ] = encontrarAmigo(amigos[ v ]);
    else return v;
}

int main(){
    int cases, i, j, n, m, dato, u, v; // n = numeroAmigos, m = numeroAmigosRestantes
    cin >> cases;
    for( i = 0; i < cases; i++ ){
        bool bandera = false;
        cin >> n >> m;
        for( j = 0; j < n; j++ ){
            cin >> dato;
            amigos[ j ] = j;
            dinero2[ j ] = 0;
            dinero1[ j ] = dato;
        }
        for( j = 0; j < m; j++ ){
            cin >> u >> v;
            if( encontrarAmigo( u ) != encontrarAmigo( v ) ){
               amigos[ encontrarAmigo( v ) ] =  amigos[ encontrarAmigo( u ) ];
            }
        }
        for( j = 0; j < n; j++ ) dinero2[ encontrarAmigo( j ) ] += dinero1[ j ];
        for( j = 0; j < n; j++ ){
            if( dinero2[ j ] != 0 ){
                bandera = true;
            }
        }
        if( ! bandera ) printf("POSSIBLE\n");
        else printf("IMPOSSIBLE\n");
    }
}
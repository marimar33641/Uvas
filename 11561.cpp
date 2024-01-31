/*
Problem name: As Long as I Learn, I Live
Maria Del Mar Villaquiran Davila
20 de septiembre 2021
*/
#include <iostream>
#include <string.h>
using namespace std;
const int MAX = 100;
char adj[ MAX ][ MAX ];
int posiciones[ 4 ][ 2 ] = {{1,0}, {0,1}, {-1,0}, {0,-1}}; //para saber la posicion de arriba, abajo, izquierda, derecha
int piezaOro;
int W,H;
void dfsAux( int i, int j ){ 
    int k, newY, newX;
    bool trampa = false;
    //printf(" %c \n",adj[ i ][ j ] );
    if( adj[ i ][ j ] == 'G' ){
        piezaOro += 1;
    }
    for( k = 0; k < 4; k++ ){
        newX =  i + ( posiciones[ k ][ 0 ] );
        newY =  j + ( posiciones[ k ][ 1 ] );
        if( adj[ newX ] [ newY ] == 'T' ){
            //encontro una trampa
            trampa = true;
        }
    }
    adj[ i ][ j ] = '#';
    //aqui iria que si no es una trampa 
    if( ! trampa ){
        for( k = 0; k < 4; k++ ){
            newX =  i + ( posiciones[ k ][ 0 ] );
            newY =  j + ( posiciones[ k ][ 1 ] );
            if( newX >= 0 && newX < H && newY >= 0 && newY < W && adj[ newX ] [ newY ] != '#' ){
                dfsAux( newX, newY );
            }
        }
    } 
}

int main(){
    int i, j;
    while( scanf( "%d %d", &W, &H ) == 2 ){
        piezaOro = 0;
        for( i = 0; i < H; i++ ){
            scanf("%s", adj[ i ] ); 
        }    
        for(i = 0; i < H; i++ ){
            for( j = 0; j < W ; j++ ){
                if( adj[ i ][ j ] == 'P' ){
                    dfsAux( i, j );
                }
            }
        }
        printf("%d\n", piezaOro );    
    }
    return 0;
}
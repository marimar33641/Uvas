#include <iostream>
#include <cstdio>
/*
Maria del mar Villaquiran Davila
26 de agosto 2021

POPES
*/
using namespace std;
int main(){
    int n, anios;
    while( scanf( "%d", &anios ) != EOF ){ //Cantidad años
        scanf("%d", &n);//Numero de papas
        int vals[ n ];
        for( int i = 0; i < n; ++i ) {  //Guardo en una lista los años de eleccion de los papas
            scanf("%d", &vals[i]);
        }
        int low, high, v = 0, l = 0, j;
        for( int i = 0; i < n; ++i ) {
            j = i;
            while( vals[ j ] < vals[ i ] + anios ) {
                l++;
                j++;
            }
            if( l > v ){ // Compara el l con el mayor, o sea v (un swap). Si l es mayor que v, pues el mayor que es v, pasaria a ser l.
                v = l;
                low = vals[ i ];
                high = vals[ j - 1 ];
            }
            l = 0;
        }
        printf("%d %d %d\n", v, low, high );
    }
    return 0;
}
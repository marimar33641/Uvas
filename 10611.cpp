#include <iostream>
#include <cstdio>
#include <string>
/*
Maria Del Mar Villaquiran Davila
27 Agosto - 5 de Septiembre
*/
using namespace std;

int busquedaBinariaHigh( int alturaN[], int alturaQ, int * x ){
    int low = 0, high = *x -1; //Low desde 0 y el high desde el tamaño de N
    while( low <= high ){ //Mientras el low sea menor al high :D
        int mid = ( low + high ) / 2; //Se hace lo del punto medio 
        if( alturaN[mid] <= alturaQ ){ //Si la lista de alturas N en la posicion mid (recorrer la lista de alturas N) y si es menor o igual a la alturaQ, a la que se ingreso, pues el Low pasará a ser mid + 1, o sea una posicion mas allá del mid.
            low = mid + 1;
        }
        else if( alturaN[mid] > alturaQ ){ //Si la lista de alturas N en la posicion mid (recorrer la lista de alturas N) y si es mayor a la alturaQ, a la que se ingreso, pues el high pasará a ser mid - 1, o sea una posicion menos allá del mid
            high = mid - 1;
        }
    }
    if( low >= *x ) { //Si el low es igual a la cantidad de Lady chimps pues va a retornar 0 para imprimir X, ya que no lo encontro
        return 0;
    }
    return alturaN[ low ]; //Y se retorna la alturaN de low
}

int busquedaBinariaLow( int alturaN[], int alturaQ, int * x ){
    int low = 0, high = *x - 1;//Low desde 0 y el high desde el tamaño de N
    while( low <= high ){//Mientras el low sea menor al high :D
        int mid = ( low + high ) / 2;//Se hace lo del punto medio 
        if( alturaN[mid] < alturaQ ){//Si la lista de alturas N en la posicion mid (recorrer la lista de alturas N) y si es menor a la alturaQ, a la que se ingreso, pues el Low pasará a ser mid + 1, o sea una posicion mas allá del mid.
            low = mid + 1;
        }
        else if( alturaN[mid] >= alturaQ ){//Si la lista de alturas N en la posicion mid (recorrer la lista de alturas N) y si es mayor a la alturaQ, a la que se ingreso, pues el high pasará a ser mid - 1, o sea una posicion menos allá del mid
            high = mid - 1;
        }
    }
    if( high < 0) { //Si el High es < 0, significa pues va a retornar 0 para imprimir X, ya que no lo encontro
        return 0;
    }
    return alturaN[ high ]; //Y se retorna la alturaN de high
}

int main(){
    int n, i, numeroConsultas, alturaQ, x; 
    scanf( "%d", &n );
        int alturaN[ n ];
        for( i = 0; i < n; ++i ){
            cin >> alturaN[ i ]; // Se agrega las alturas N
        }
        scanf("%d", &numeroConsultas);
        x = n;
        for( i = 0; i < numeroConsultas; ++i ){
            cin >> alturaQ;
            int a = busquedaBinariaLow( alturaN, alturaQ, &x ); // Se hace busqueda binaria de low
            int b = busquedaBinariaHigh( alturaN, alturaQ, &x );  // Se hace busqueda binaria de high
            if( a == 0 ){ //Si la funcion retorna 0, significa que no encontro ninguna de esas dos estaturas
                printf("X ");
            }
            else{
                printf("%d ", a);
            }
            if( b == 0 ){//Si la funcion retorna 0, significa que no encontro ninguna de esas dos estaturas
                printf("X\n");
            }
            else{
                printf("%d\n", b);
            }    
        }
    return 0;
}
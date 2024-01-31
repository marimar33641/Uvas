/*
Maria Del Mar Villaquiran Davila
6 de agosto 2021
*/

#include <iostream>
#include <list>
using namespace std;

int prioridadValor( list<int> prioridad ){ //Comprobar la prioridad en la que se encuentra el elemento
    list<int>::iterator elemento = prioridad.begin();
    for( list<int>::iterator it = prioridad.begin(); it != prioridad.end(); it++ ){ //Recorrer la lista, desde el elemento que se creo hasta que sea diferente al final
        if( *elemento < *it ){
            return 1; //Si el elemento que esta al inicio es menor al iterador, va a retornar 1, para comprobar
        }
    }
    return 0;
}

int main(){
    list<int> listaTiempo;
    int cases, i;
    scanf( "%d", &cases );
    for( i = 0; i < cases; i++ ){
        list<int> prioridad;
        list<int>::iterator elemento1;
        list<int>::iterator elemento2;
        int cases, i, n, m, j, valor, valor2, k, tiempo = 0;
        bool alt = true;
        cin >> n >> m;
        for( j = 0; j < n; j++ ){
            cin >> valor;
            prioridad.push_front(valor);
        }
        
        prioridad.reverse(); //recorrer bien la lista 1 2 3 4 (ejemplo)
        //imprimirLista(prioridad);
        list<int>::iterator it = prioridad.begin(); //El primero

        for( j = 0; j < m; j++ ){
            it++;
        }
        while( alt != false ){
            elemento1 = prioridad.begin(); //El iterador elemento1 va a ser el primero de la lista de prioridad
            if( prioridadValor( prioridad ) && it == elemento1 ){ //mandarlo para atras 
                /*
                Hace que guarde el primer elemento para mandarlo para atras (Hacer algo como swap, guardar la variable)
                para borrarla en el front y mandarla para el back, y se le suma al iterador de la lista de prioridad
                */
                elemento2 = prioridad.begin();
                valor2 = *elemento2;
                prioridad.pop_front();
                prioridad.push_back( valor2 );
                it = prioridad.begin();
                for( j = 0, k = prioridad.size() - 1; j < k ; j++ ){
                    it++;
                }  
            }
            else if( prioridadValor( prioridad ) && it != elemento1 ){
                /*
                Hace el iterador elemento2 sea el primer elemento, para poder borrarlo del front y mandarlo para atras
                */
                list<int>::iterator elemento2 = prioridad.begin();
                valor2 = *elemento2;
                prioridad.pop_front();
                prioridad.push_back( valor2 );
            }
            
            else if( !prioridadValor( prioridad ) && it != elemento1 ){ //Si no se comprueba que hay una prioridad mayor a la anterior, y que el it que es el primero es diferente al iterador elemento 1 es diferente, se borra el elemento y se le suma 1 min 
                    prioridad.pop_front();
                    tiempo++;
            }
            else{
                break;
            }
        }
        tiempo++;
        listaTiempo.push_back(tiempo);
    }
    for(list<int>::iterator it = listaTiempo.begin(); it != listaTiempo.end(); it++){ //Imprimir la lista
        cout<< *it << endl; 
    }
}
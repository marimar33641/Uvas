/*
Maria Del Mar Villaquiran Davila
3 de agosto 2021
*/

#include <iostream>
#include <stack>
#include <string>
using namespace std;
int k = 0;
int main(){
    string cases;
    int error, i, j;
    while( getline(cin, cases) ){
        error = 0;
        stack<char> pil;
        for( i = 0, j = cases.size(); i < j; i++ ){  //Cantidad(Tamanio) de la cadena que se ingreso
        if( cases[ i ] == '{' || cases[ i ] == '[' || cases[ i ] == '<' ){ //Si se encuentra alguno de esos
            pil.push( cases[i] );
        }
        else if( cases[ i ] == '(' ){ //Verificando el (*
            if( cases[ i + 1 ] == '*' ){
                pil.push('a');
                i++;
            }
            else{
                pil.push('('); //Si no hay en la posicion [ i + 1 ] un * entonces es (
            }
        }
        else if( cases[ i ] == '*' ){ //Ya para cerrar el *)
            if( cases[ i + 1 ] == ')' ){
                if( pil.empty() || pil.top() != 'a' ){
                    break;
                }
                pil.pop();
                i++;  
            }
        }
            //Cerrando (otro lado) con todos los casos
            else if( cases[ i ] == '}' || cases[ i ] == ']'  || cases[ i ] == '>' || cases[ i ] == ')' ){
                if( pil.empty() ){ 
                    break;
                }
            if( cases[ i ] == ']' ){
                if( pil.top() != '[' ){
                    
                    break;
                }
                else{
                    pil.pop();
                }
            }
             if( cases[ i ] == ')' ){
                if( pil.top() != '(' ){
                    break;
                }
                else{
                    pil.pop();
                }
             }
            if( cases[ i ] == '}' ){
                if( pil.top() != '{' ){
                    break;
                }
                else{
                    pil.pop();
                }
            }
            if( cases[ i ] == '>' ){
                if( pil.top() != '<' ){
                    break;
                }
                else{
                    pil.pop();
                }
            }
        }
            error++;
    	}
        if( i < cases.size() || !pil.empty() ){
        	error++;
            cout << "NO " << error << endl;
        } 
        else {
            cout << "YES"<<endl;
        }
    }
}
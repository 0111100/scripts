#include <stdio.h>

int main()
{
    //Pide un numero del 1 al 5 y di si es primo o no
    int n;
    printf("Introduce un numero del 1 al 5: ");
    scanf("%d",&n);
        
    if (n!=4){
        printf("Es un numero primo");
    }
    else{
        printf("No es un numero primo");
    }
    
    return 0;
}

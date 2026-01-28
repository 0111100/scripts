#include <stdio.h>

int main()
{
    //Pide un numero del 1 al 5 y di si es primo o no
    int n;
    printf("Introduce un numero del 1 al 5: ");
    scanf("%d",&n);
        
    if (n!=4){
        printf(" %d es un numero primo",n);
    }
    else{
        printf(" %d no es un numero primo",n);
    }
    
    return 0;
}

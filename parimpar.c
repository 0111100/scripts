#include <stdio.h>

int main()
{
    // Pide un número y di si es par o impar
    int n;
    printf("Introduce un numero: ");
    scanf("%d",&n);
        
    if (n%2==0){
        printf(" %d es par",n);
    }
    else{
        printf(" %d no es par",n);
    }
    
    return 0;
}

#include <stdio.h>

int main()
{
    // Pide una letra y determina si es vocal o no.
    
    char c;
    printf(" Introduce una letra: ");
    scanf("%c",&c);
    
    if( c == 'a' || c == 'A' || c == 'e' || c == 'E' || c == 'i' || c == 'I' || c =='o' || c == 'O' || c == 'u' || c == 'U'){
        printf(" La letra %c es una vocal",c);
    }
    else{
        printf(" La letra %c no es una vocal",c);
    }
    return 0;
}

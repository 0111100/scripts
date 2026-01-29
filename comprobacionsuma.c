#include <stdio.h>

int main()
{
    // Pide dos numeros y sumalos, haz que el usuario ponga el resultado y comprueba que sea correcto su input.
    
    int n1;
    printf(" Introduce un numero: ");
    scanf("%d",&n1);
    
    int n2;
    printf(" Introduce un numero: ");
    scanf("%d",&n2);
    
    int ru;
    printf("\n Cual es el resultado de la suma de ambos numeros?: ");
    scanf("%d",&ru);
    
    int r;
    r = n1 + n2;
    
    if(ru == r){
        printf(" La respuesta es correcta");
    }
    
    else{
        printf(" La respuesta es incorrecta");
    }
    
    return 0;
}

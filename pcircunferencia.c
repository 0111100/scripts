#include <stdio.h>

int main()
{
    // Calcula el perimetro de la circunferencia segun el radio o el diametro.
    
    int r;
    printf("Introduce el radio de la circunferencia: ");
    scanf("%d",&r);
    
    //calgulo con radio
    float pi = 3.141592;
    float pr = 2 * pi * r;
    printf("\n El perimetro de la circunferencia segun el radio es: %.5f ", pr);
    
    //calculo con diametro
    float d = 2 * r;
    float pd = pi * d;
    printf("\n El perimetro de la circunferencia segun el diametro es: %.5f ", pd);
    return 0;
}

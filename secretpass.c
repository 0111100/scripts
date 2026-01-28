#include <stdio.h>
#include <string.h>

int main()
{
    // Solo permite introducir la palabra wubbalubbadubdub.
    
    char n[20];
    printf("Introduce la palabra secreta: ");
    scanf("%s",&n);
        
    if (strcmp(n, "wubbalubbadubdub") == 0){
        printf("Correct secret, but shhhhh!!");
    }
    
    else{
        printf("Incorrect secret");
    }
    
    return 0;
}

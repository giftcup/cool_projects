#include <stdio.h>
#include <time.h>

int main()
{
    srand(time(NULL));
    
    int guess = (rand() % 10) + 1, num;

    printf("Guess a number between 1 and 10 inclusive: ");
    scanf("%d", &num);

    while(num != guess)
    {
        if(num < guess)
        {
            printf("The number you guessed is smaller than the number the computer guessed\nTry again: ");
            scanf("%d", &num);
        }
        else if( num > guess)
        {
            printf("The number you guessed is bigger than the number the computer guessed\nTry again: ");
            scanf("%d", &num);
        }
    }

    printf("Congratulations!! You guessed correctly");
}

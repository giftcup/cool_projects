#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main (int argc, char *argv[])
{
    char plaintext[100], ciphertext[100];

    //checkind if the correct number of arguments are entered
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    //checking if every character in the key is a digit.
    for (int i = 0, n = strlen(argv[1]); i < n; i++)
    {
        if (isdigit(argv[1][i]) == 0)
        {
            printf("Usage: ./caesar key\nThe key should consist of deigits only");
            return 1;
        }
    }

    int key;
    /*argv[] stores a string of characters
    * atoi() converts the string to integers */
    key = atoi(argv[1]);

    printf("Plaintext: ");
    fgets(plaintext, sizeof(plaintext), stdin);
    
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        //wrapping around alphabetical characters
        if (plaintext[i] > 96 && plaintext[i] < 123)
        {
            plaintext[i] -= 97;
            ciphertext[i] = (plaintext[i] + key) % 26;
            ciphertext[i] += 97;
        }
        else if(plaintext[i] > 64 && plaintext[i] < 91)
        {
            plaintext[i] -= 65;
            ciphertext[i] = (plaintext[i] + key) % 26;
            ciphertext[i] += 65;
        }
        else
        {
            ciphertext[i] = plaintext[i];
        }
    }

    //Prints out the coded text
    printf("Ciphertext: %s\n", ciphertext);

    return 0;
}
//Converts Plaintext into ciphertext with caesar cipher (takes key in as a command line argument)
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        for (int i = 0; i < strlen(argv[1]); i++)
        {
            if (isdigit(argv[1][i]) == false)
            {
                printf("Usage: ./caesar key\n");
                return 1;
            }
        }
        int key = atoi(argv[1]);
        string cText = get_string("plaintext: ");
        printf("ciphertext: ");

        int ctextlen = strlen(cText);
        for (int _ = 0; _ < ctextlen; _++)
        {
            if (cText[_] >= 'a' && cText[_] <= 'z')
            {
                printf("%c", (((cText[_] - 'a') + key) % 26) + 'a');
            }
            else if (cText[_] >= 'A' && cText[_] <= 'Z')
            {
                printf("%c", (((cText[_] - 'A') + key) % 26) + 'A');
            }
            else
            {
                printf("%c", cText[_]);
            }
        }
        printf("\n");
        return 0;
    }
    else
    {
        return 1;
    }
}
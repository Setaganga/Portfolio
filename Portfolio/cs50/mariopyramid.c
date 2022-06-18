//Makes a pyramid with a gap in between. Similar to that in mario: https://miro.medium.com/max/1400/1*N8gBpZ26hbjw4tqvrDeYkQ.png
#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n = 0;
    do
    {
        n = get_int("Height:"); //Loop to force user to not be stupid
    }
    while (n < 1 || n > 8); //Basically only allows 1,2,3,4,5,6,7 and 8 only

    for (int i = 0; i < n; i++)
    {
        for (int _ = 0; _ < (n - i) - 1; _++) //The equation n - i - 1, if i = 0 and height is 8: 8 - 0 - 1 = 7 (you need 7 spaces)
        {
            printf(" ");
        }
        for (int j = 0; j < n - ((n - i) - 1); j++) // From example case earlier: 8 - (7) = 1 (One hashtag)
        {
            printf("#");
        }
        printf("  "); //Gap
        for (int k = 0; k < n - ((n - i) - 1); k++) //The same thing with lines 19-22
        {
            printf("#");
        }
        printf("\n"); //Line break
    }
}
/*
Calculates the grade level of a piece of text based off the formula below
index = 0.0588 * L - 0.296 * S - 15.8
where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
*/
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>
#include <math.h>

int main(void)
{
    //Get text from user
    string text = get_string("Enter text: ");

    //Counts
    int lettercount = 0;
    int sentencecount = 0;
    int wordcount = 1;
    //Runs for entire text
    for (int i = 0, length = strlen(text); i < length; i++)
    {
        //If letter, increment letter count
        if (isalpha(text[i]))
        {
            lettercount++;
        }
        //If has a space, increment word count (words separated by spaces)
        else if (text[i] == ' ')
        {
            wordcount++;
        }
        //If has a . ! or ? add to sentence count (sentences end in such characters)
        else if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            sentencecount++;
        }
    }
    //Formula stuff
    float L = lettercount / (float) wordcount * 100;
    float S = sentencecount / (float) wordcount * 100;
    int index = round(0.0588 * L - 0.296 * S - 15.8);

    //Print out appropriate grade levels
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %i\n", index);
    }
}
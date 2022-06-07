/*
This program filters how many coins are needed for change.
Originally it only shows the amount of coins needed, but I just made it print out the
number of the specific coins as well
*/
#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = 0;
    do
    {
        cents = get_int("Cents:"); //Loop to force user to not be stupid
    }
    while (cents < 0);

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("Quarters:%i,Dimes:%i,Nickels:%i,Pennies:%i",quarters,dimes,nickels,pennies);
    printf("%i\n", coins);
}

int get_cents(void)
{
    int inCents = get_int("How many cents? ");
    return inCents;
}

int calculate_quarters(int cents)
{
    int returnval = 0;
    while (cents / 25 >= 1)
    {
        returnval++;
        cents -= 25;
    }
    return returnval;
}

int calculate_dimes(int cents)
{
    int returnval = 0;
    while (cents / 10 >= 1)
    {
        returnval++;
        cents -= 10;
    }
    return returnval;
}

int calculate_nickels(int cents)
{
    int returnval = 0;
    while (cents / 5 >= 1)
    {
        returnval++;
        cents -= 5;
    }
    return returnval;
}

int calculate_pennies(int cents)
{
    int returnval = 0;
    while (cents / 1 >= 1)
    {
        returnval++;
        cents -= 1;
    }
    return returnval;
}

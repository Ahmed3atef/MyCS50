#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
     // get user input
         n = get_int("Height: ");
     // loop until user coop
    while(n > 8 || n < 1);
    for (int i = 0; i < n; i++)
    {
        for (int j = n - 1; j > i; j--)
        {
            printf(" ");
        }
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}

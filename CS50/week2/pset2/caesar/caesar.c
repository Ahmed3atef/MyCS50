#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>




int main(int argc, string argv[])
{
    // variabels
    bool run = false;
    int key = 0;
    // check how many arguments in command line
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    else
    {
        // get the key
        for (int x = 0; x < argv[1][x]; x++)
        {
            char C = argv[1][x];

            if (C >= 48 && C <= 57)
            {
                key = atoi(argv[1]);
                while (key > 26)
                {
                    key = (key - 26);
                }
                run = true;
            }
            else
            {
                printf("Usage: ./caesar key\n");
                run = false;
                return 1;
                break;
            }
        }
    }
    //check evrydigit and add the key to it
    if (run == true)
    {
        string text = get_string("plaintext: ");
        printf("ciphertext: ");
        for (int i = 0, z = strlen(text); i < z; i++)
        {
            int L = (text[i] + key);
            if ((text[i] >= 65 && text[i] <= 90) || (text[i] >= 97 && text[i] <= 122))
            {
                if ((L > 90 && L < 97) || (L > 122))
                {
                    if ((text[i] >= 65 && text[i] <= 90))
                    {
                        char Ci = L % 90;
                        Ci = Ci + 64;
                        printf("%c", Ci);
                    }
                    else if ((text[i] >= 97 && text[i] <= 122))
                    {
                        char Ci = L % 122;
                        Ci = Ci + 96;
                        printf("%c", Ci);
                    }
                }
                else
                {
                    printf("%c", L);
                }
            }
            else
            {
                printf("%c", text[i]);
            }
        }
        printf("\n");
    }

}

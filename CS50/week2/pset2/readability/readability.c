#include <stdio.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

// arithmatic func
double readability_test(double L, double S, double W);

int main(void)
{

    // get the letter from user
    string s = get_string("Text: ");

    //variabile for store letter words sentences and length of them
    double wol = strlen(s), letter = 0, word = 0, sentence = 0;
    bool key = true;

    // loop for checking for evry char in letter and count it
    for (int i = 0; i < wol + 1; i++)
    {


        if ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122))
        {
            letter ++;
        }

        if (s[i] == 32)
        {
            key = true;
        }
        else
        {
            if (key == true && ((s[i] >= 65 && s[i] <= 90) || (s[i] >= 97 && s[i] <= 122)))
            {
                word ++ ;
                key = false;
            }
        }


        if (s[i] == 63 || s[i] == 46 || s[i] == 33)
        {
            sentence ++;
        }




    }


    double sum = readability_test(letter, sentence, word);

    // print the grade of letter
    if (sum < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (sum > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %1.0f\n", sum);
    }
}

//Coleman–Liau index to get grade of letter
double readability_test(double L, double S, double W)
{
    double avg_L = (L / W) * 100;
    double avg_S = (S / W) * 100;
    double total = ((0.0588 * avg_L) - (0.296 * avg_S) - 15.8);
    return total;
}
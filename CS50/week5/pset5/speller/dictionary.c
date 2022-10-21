// Implements a dictionary's functionality

#include <string.h>
#include <strings.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <stddef.h>
#include <stdbool.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

int wordCount = 0;
// Number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary else false
bool check(const char *word)
{
    int key = hash(word);
    
    node *nodeptr = table[key];
    
    while(nodeptr != NULL)
    {
        
        if (strcasecmp(nodeptr->word, word) == 0)
        {
            return true;
        }
        
        nodeptr = nodeptr->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
   int value = 0;
   
   for (int i = 0; word[i] != '\0'; i++)
   {
       value += tolower(word[i]);
   }
    return value % N;
}

// Loads dictionary into memory, returning true if successful else false
bool load(const char *dictionary)
{
    FILE *fileptr = fopen(dictionary, "r");
    if (fileptr == NULL)
    {
        return false;
    }
    
    for (int i = 0; i < N; i++)
    {
        table[i] = NULL;
    }
    
    char tempMord[LENGTH + 1];
    
    while(fscanf(fileptr, "%s\n", tempMord) != EOF)
    {
        node *tempNode = malloc(sizeof(node));
        
        strcpy(tempNode->word, tempMord);
        
        int key = hash(tempMord);
        
        if(table[key] == NULL)
        {
            tempNode->next =NULL;
            table[key] = tempNode;
        }
        else
        {
            tempNode->next = table[key];
            table[key] = tempNode;
        }
        
        wordCount++;
    }
    
    fclose(fileptr);
    return true;
}

// Returns number of words in dictionary if loaded else 0 if not yet loaded
unsigned int size(void)
{
    return wordCount;
}

// Unloads dictionary from memory, returning true if successful else false
bool unload(void)
{
    for(int i = 0; i < N; i++)
    {
        node *nodeptr = table[i];
        
        while (nodeptr != NULL)
        {
            node *deletMe = nodeptr;
            nodeptr = nodeptr->next;
            free(deletMe);
        }
        table[i] = NULL;
    }
    return true;
}

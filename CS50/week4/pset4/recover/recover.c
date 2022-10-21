#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>
#include <stdint.h>

//define new data type (works with bytes)
typedef uint8_t BYTE;

//make some constints (the size of one block , and the size of file name)
#define BLOCK_SIZE 512
#define FILE_NAME_SIZE 8

//the func that help us to knowing if this array of bytes is jpeg file or not
bool is_start_new_jpeg(BYTE buffer[]);


int main(int argc, char *argv[])
{
    //error massage
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    
    //open the file 
    FILE *infile = fopen(argv[1], "r");
    
    //check the file 
    if (infile == NULL)
    {
        printf("File Not Found\n");
        return 1;
    }
    
    //set byte buffer
    BYTE buffer[BLOCK_SIZE];
    
    //set counter of file names 
    int file_index = 0;
    
    //the switch
    bool have_found_first_jpg = false;
    
    //open the recover file to copy old info
    FILE *outfile;
    
    while (fread(buffer, BLOCK_SIZE, 1, infile))
    {
        if (is_start_new_jpeg(buffer))
        {
            if (!have_found_first_jpg)
            {
                have_found_first_jpg = true;
            }
            else
            {
                fclose(outfile);
            }
            
            char filename[FILE_NAME_SIZE];
            
            sprintf(filename, "%03i.jpg", file_index++);
            
            outfile = fopen(filename, "w");
            
            if (outfile == NULL)
            {
                return 1;
            }
            
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
            
        }
        else if (have_found_first_jpg)
        {
            //keep on writing the previous file
            fwrite(buffer, BLOCK_SIZE, 1, outfile);
        }
    }
    //close all files
    fclose(outfile);
    fclose(infile);
}

//check the file blocks if is it jpeg or not
bool is_start_new_jpeg(BYTE buffer[])
{
    return buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0;
}
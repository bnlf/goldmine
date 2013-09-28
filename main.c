/* 
* MAC0425/5730 - Inteligencia Artificial - EP1 @ 2013.2
* Autor: Bruno Nunes Leal Faria - nUSP: 8765551
*
* FILE: main.c
*/

#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>

int main(int argc, char** argv) 
{
	int n;
	char** mineField;
	char* fileName;

	// check number of parameters 
	if(argc != 3) {
		printf("Uso: <arquivo_de_entrada> <tipo_de_busca>\n");
		printf("Tipo de busca: L (largura), P (profundidade) ou A (A*)\n");
		exit(1);
	} 

	// check if type of search is valid
	if(strcmp(argv[2], "L") != 0 && strcmp(argv[2], "P") != 0 && strcmp(argv[2], "A") != 0) {
		printf("Tipo de busca nao suportado\n");
		printf("Tipo validos: L (largura), P (profundidade) ou A (A*)\n");
		exit(2);
	}

	// check if file exists
	fileName = argv[1];
	if(file_exist (fileName))
	{
		// check if file is valid and reads it
		readInput(fileName, mineField, n);
	} else {
		printf("arquivo nao encontrado\n");
	}
	return 0;
}

int file_exist(char* filename)
{
  	struct stat buffer;   
  	return (stat (filename, &buffer) == 0);
}

void readInput(char* filename, char* mineField, int n)
{
	FILE* fp = fopen(filename, "r");
	char c;

	// check if file is readable
	if (fp == NULL) {
		exit(EXIT_FAILURE);
	}
    
    // reads the file
    fscanf (fp, "%d", &n);

    // initialization
    //mineField = char*[n];

    // first line, size of mine 1<=x<=50
    for (int i=0; i<n; i++) 
    {
        mineField[i] = char[n];
    }
    
    // read first line break
    fscanf (fp, "%c", &c); 
    
    // line
    for(int i=0; i<n; i++)
    {
    	// column
        for(int j=0; j<n; j++) 
        { 
            fscanf (fp, "%c", &c);
            mineField[i][j]=c;
        }
        // reads line break before continuing
        fscanf (fp, "%c", &c); 
    }

    fclose(fp);
    fp=0;
}


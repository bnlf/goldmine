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
#include <unistd.h>

int main(int argc, char** argv) {
  
  	FILE * fp;
	char * line = NULL;
	int c;
	
	if(argc != 3) {
		printf("Uso: <arquivo_de_entrada> <tipo_de_busca>\n");
		printf("Tipo de busca: L (largura), P (profundidade) ou A (A*)\n");
		exit(1);
	} 

	if(strcmp(argv[2], "L") != 0 && strcmp(argv[2], "P") != 0 && strcmp(argv[2], "A") != 0) {
		printf("Tipo de busca nao suportado\n");
		printf("Tipo validos: L (largura), P (profundidade) ou A (A*)\n");
	}

	if(file_exist (argv[1]))
	{
	  	fp = fopen(argv[1], "r");
		if (fp == NULL)
		   exit(EXIT_FAILURE);

		while ((c = fgetc(fp)) != EOF) {
			putchar(c);
		}

		if (line)
		   free(line);
		exit(EXIT_SUCCESS);
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


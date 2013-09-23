### Inteligência Artificial – Exercício Programa 1 ###

Mina de Ouro

### Ambiente ###

Mina - n x n, 1 = obstáculo, * = ouro, 0 = livre
 
Quantidade de ouro: n/2

Custo do passo: 1

Ganho do ouro: 4n

Ações: (D)ireita, (E)squerda, (C)ima, (B)aixo, (P)egar

### Objetivos ###

- Um ambiente de avaliação, que recebe as ações do agente e calcula sua
pontuação. O ambiente é acessível e determinístico.
- Um agente resolvedor de problemas.
- Pelo menos tr^es estratégias de busca: largura, profundidade (com limite) e A*.

Main.java (main.c): Seu programa receberá como argumentos a localização do arquivo de teste.

Ambiente.java (ambiente.c): implementação do ambiente mina. Sua descrição deve conter os elementos de uma 
descrição PEAS, ou seja, descrição do estado, dos sensores e atuadores, dos efeitos da atuação de um
agente no ambiente, cálculo da medida de desempenho, etc.

Agente.java (agente.c): implementação do agente. Deve conter a implementação do programa agente, da percepção dos
sensores, da interação com o ambiente (atuadores), etc.

### Entrada ###

    main.c <arquivo_de_teste> <tipo_de_busca>

- Formato do arquivo de teste: primeira linha do arquivo contém um inteiro 1 ≤n≤ 50 que indica o tamanho da mina; as n linhas seguintes descrevem uma matriz de caracteres n×n que representa: 0 posição livre, 1 posição com obstáculo e * posição com ouro.
- Estratégia de busca: indicada por uma única letra: L para busca em largura; P para busca em profundidade com limite; e A para A*.

### Relatório ###

- uma breve descrição das principais classes e funçoes de sua implementação;
- descrição da heurística utilizada no A* e justificativa de sua escolha;
- informaçoes sobre testes e análise do desempenho das diferentes buscas.

### Entregar ###

- Um único arquivo zipado, contendo:
- Código fonte da implementação;
- Um relatório, em pdf.

### Exemplo de teste ###

    8
    0000100*
    11101011
    00001010
    *0111000
    00000000
    11101110
    00100*10
    0000001*

### Exemplo de saída ###

    70 pontos
    D D D B B E E E B P D B D D D D C C C C D D P E E B B B D D B
    B B B P C C C E E E E B B D D P E E C C E E C C D D C C E E E

	

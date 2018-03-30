<h1>Algoritmo de Ordenação</h4> <br>
<p align="center">    
    <img src="http://2.bp.blogspot.com/-0LbmcxSHWao/VAj-ZMSSKYI/AAAAAAAAXS4/5UvH13jPCJM/s1600/escadinha.jpg" width=700 height=400>
</p>

## Contribuidores
| Nome	| Matrícula	|
|--|--|
| Adrianne Alves da Silva | 16/0047595 |
| Lucas Arthur Lermen | 16/0012961 |


## Apresentação

Este repositório apresenta um algoritmo de ordenação, o insertion sort, escrito em linguagem c, para fins didáticos na disciplina de Estrutura de dados 2. Consiste em uma atividade apresentada como avaliação parcial da disciplina de Estrutura de dados 2 do curso de Engenharia de software da Universidade de Brasília (UnB), Campus de Engenharias - Faculdade do Gama (FGA).

## Sobre algoritmo de ordenação

Algoritmos de ordenação, como o próprio nome explicita, refere-se à estruturas lógicas que independente da linguagem é capaz de ordenar um dado, seja em ordem crescente ou decrescente. Em geral, cada tipo de algoritmo possui uma abordagem diferenciada, por esse motivo, segue abaixo uma explicação suscinta a respeito do insertion sort.


### 1.0 Diferentes tipos de ordenação com complexidade O(n²)

Existem variadas maneiras de realizar a ordenação de um dado, as mais simples delas, que foram construídas por meio da observação do processo natural de ordenação, concentram-se em encontrar o maior ou menor número do vetor e levá-lo até a sua posição. Dentre estes estes algorítmos, encontram-se o selection sort, o insertion sort, o bubble sort e o shell sort.

O selection sort inicia a caçada na posição 0 do vetor, considerando-o como o menor elemento e compara-o aos demais elementos do vetor, trazendo assim para a sua primeira posição o valor correto, e assim por diante O bubble sort , como o nome propõe funciona por borbulhamento, de modo que o último fica ordenado em cada iteração do algoritmo, comparando o elemento com o seu vizinho até que o mesmo atinja a sua posição. Já o shell sort funciona por gap, de modo que a cada iteração o gap é dividido por uma razão de 2 de modo a formar diferentes conjuntos a serem ordenados.

Segue abaixo alguns exemplos das três tecnologias apresentadas:

Selection Sort

![alt text](http://codepumpkin.com/wp-content/uploads/2017/10/SelectionSort_Avg_case.gif)

Bubble Sort

![alt text](http://codepumpkin.com/wp-content/uploads/2017/10/BubbleSort_Avg_case.gif)

Shell Sort

![alt text](http://parallelcomp.uw.hu/files/09fig44.gif)

Um algoritmo que faltou ser falado foi o insertion sort, objetivo de estudo da implementação deste repositório, que será explicado na seção a seguir.

### 1.1 Ordenação utilizando o Insertion Sort

O insertion sort é considerado um algoritmo simples e natural, pois remonta o nosso costume ou maneira automática de organizar um conjunto de números.Consiste basicamente em procurar o local ou o lugar de um número e realocar todo o resto para incorporá-lo ao lugar correto. Esse comportamento pode ser observado por meio da imagem a seguir.

![alt text](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)

### Algoritmo implementado

Com fins didáticos, o algoritmo implementado aqui corresponde à uma ordenação através do insertion sort com vetor preenchido por valores aleatórios, em que o tamanho do mesmo será mudado a fim de medir a velocidade do algoritmo. Dessa forma, será gerado gráfico de modo a demonstrar visualmente a complexidade O(n²) do algoritmo. 

A dupla optou também por utilizar o algoritmo bubble sort para realizar uma comparação entre ambos. De modo que os dois são de complexidade O(n²), de modo que a diferença fica explícita nos gráficos mostrados na seção de resultados.

### Como utilizar

Levando em consideração que o sistema usado seja linux, basta entrar na pasta pelo terminal e digitar gcc -o exec SortingAlgorithm.c para utilizar o ordenador. O gerador de gráfico foi desenvolvido em python, assim, basta digitar no terminal python3 gerandoGraficos.py.

### Resultados 

Para coletar o tempo de execução do algoritmo a ser analisado utilizou-se a coleta do clock inicial e final e a fórmula expressa no pedaço de código a seguir, para capturar em até milisegundos : 

'''
clock_t tempo;
	tempo = clock();
  
  int i, j, aux;
  for (i = 1; i < TAMREGISTROS; i++) {
    for (j = 0; j < TAMREGISTROS - 1; j++) {
      if (registros[j] > registros[j + 1]) {
        aux = registros[j];
        registros[j] = registros[j + 1];
        registros[j + 1] = aux;
      }
    }
  }
  
  printf("Tempo:%f",(clock() - tempo) / (double)CLOCKS_PER_SEC);

'''

Assim, os valores foram destinados a dois diferentes vetores, o dedicado ao insertion sort, principal tema dessa entrega e o vetor para o bubble sort, considerando o mesmo intervalo de quantidade de registros. Nesse sentido, obteve-se o gráfico esperado através dos dados que foram coletados, conforme apresentado abaixo.

![img](https://preview.ibb.co/jTD7FS/Figure_1.png)

![img](https://preview.ibb.co/moXEUn/Figure_1.png)


Assim, sobrepondo os gráficos é possível observar que o insertion sort, em azul, apresentou um desempenho superior na ordenação dos dados aleatórios, pois a variação no tempo de execução de acordo ao aumento do número de elementos é menor que o que ocorre com o bubble sort em laranja, ou seja, ele ordena uma maior quantidade de números em um menor tempo. 


![img](https://preview.ibb.co/d3BPUn/Figure_1.png)


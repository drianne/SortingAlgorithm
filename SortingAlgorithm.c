#include<stdlib.h>
#include<stdio.h>
#include <time.h>

#define TAMREGISTROS 100000

void preencheRegistros(int *registros){
    int i;
    for (i = 0; i < TAMREGISTROS; ++i){
      registros[i] = rand() % (TAMREGISTROS+300);
    }
}

void insertionSort(int *registros){
  int i, troca, atual;
  for(i = 1; i<TAMREGISTROS; i++){
    atual = i;
    while (atual!=0){
      int anterior = atual - 1;
      if(registros[atual] < registros[anterior]){
        troca = registros[atual];
        registros[atual] = registros[anterior];
        registros[anterior] = troca;
      }
      atual = atual - 1;
    }
  }
}

void imprimeRegistros(int *registros){
  int i;
  printf("\n\nREGISTROS\n");
  printf("--------------------------------------------------------------------------------------------------------------------------------------------\n" );
  for (i = 0; i < TAMREGISTROS; i++){
    printf("%d - ",registros[i]);
  }
}

int menu(){
  int op;
  printf("\n\n\n===================================================== MENU ==================================================================\n");
  printf("1 - Ordenar vetor \n");
  printf("2 - Printar o vetor\n");
  printf("0 - SAIR");
  printf("\n\n");
  printf("Digite a opcao desejada:");
  scanf("%d", &op);
  return op;
}


int main(){

  int registros[TAMREGISTROS], opcao;

  srand(time(NULL));

  preencheRegistros(registros);

  do{
    opcao = menu();
    switch (opcao) {
      case 0: printf("Encerrando ...\n");
      break;
      case 1: insertionSort(registros);
      break;
      case 2: imprimeRegistros(registros);
      break;
      default:
        printf("Opcao Inexistente\n");
    }
  }while (opcao!=0);
  return 0;

}

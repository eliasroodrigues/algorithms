/*
  Produção Ótima de Ótima Vodka #1210

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1210

  Author: Elias E. S. Rodrigues
*/

#include <stdio.h>
#include <stdlib.h>

int main(void) {
  int periodo, idade, maxima, preco, custo[2000], venda[2001];
  int **custos, **trocas, i, j, troca, manutencao, espaco;

  while (scanf("%d %d %d %d", &periodo, &idade, &maxima, &preco) != EOF) {
    /*
      Pega os vetores de custo de manutencao e venda
      e aloca dinamicamente os vetores de custos acumulados
      e trocas.
    */
    for (i = 0; i < maxima; i++) {
      scanf("%d", &custo[i]);
    }
    for (i = 1; i <= maxima; i++) {
      scanf("%d", &venda[i]);
    }
    custos = (int**)malloc((periodo+2)*sizeof(int*));
    for (i = 1; i <= periodo+1; i++) {
      custos[i] = (int*)malloc((maxima+1)*sizeof(int));
    }
    trocas = (int**)malloc((periodo+2)*sizeof(int*));
    for (i = 1; i <= periodo+1; i++) {
      trocas[i] = (int*)malloc((maxima+1)*sizeof(int));
    }
    for (j = 0; j <= maxima; j++) {
      custos[periodo+1][j] = 0;
    }
    /*
      Calcula todas as possibilidades de troca ou manutenção durante o período
      proposto e a idade do destilador de 0 até máxima.

      Para cada (período, idade) verifica se é melhor trocar ou dar manutenção:
        trocar = preço do novo + custo da manutenção - valor da venda + custo acumulado
        manutenção = custo da manutenção + custo acumulado

      Se o valor de trocar for menor ou igual ao valor da manutenção, então é
      recomendado trocar. É adicionado na lista de custos e trocas, os valores:
        custos[período, idade] = valor de trocar
        trocas[período, idade] = True, pq foi trocado
      Caso contrário é recomendado dar manutenção, então é armazenado o
      valor acumulado da manutenção na lista custos.
        custos[(período, idade)] = valor da manuteção
    */
    
    for (i = periodo; i >= 1; i--) {
      for (j = 0; j < maxima; j++) {
        troca = preco + custo[0] - venda[j] + custos[i+1][1];
        manutencao = custo[j] + custos[i+1][j+1];

        if (troca <= manutencao) {
          custos[i][j] = troca;
          trocas[i][j] = 1;
        } else {
          custos[i][j] = manutencao;
          trocas[i][j] = 0;
        }
      }
      /*
        Quando o destilador chega a idade máxima, então tem que trocar
        obrigatoriamente.
      */
      troca = preco + custo[0] - venda[j] + custos[i+1][1];
      custos[i][j] = troca;
      trocas[i][j] = 1;
    }
    printf("%d\n", custos[1][idade]);
    /*
      Verifica os valores dos períodos onde houve troca e monta
      a saída de anos. Os anos de troca são as posições [período, idade],
      onde o período e a idade do destilador foram trocados e que estão
      dentro do período proposto.
    */
    espaco = 1;
    for (i = 1, j = idade; i <= periodo; i++) {
      if (trocas[i][j] == 1) {
        if (!espaco) {
          printf(" ");
        }
        espaco = 0;
        printf("%d", i);
        j = 1;
      } else {
        j++;
      }
    }

    if (espaco) {
      printf("0");
    }
    printf("\n");
    for (i = 1; i <= periodo+1; i++) {
      free(custos[i]);
    }
    free(custos);

    for (i = 1; i <= periodo+1; i++) {
      free(trocas[i]);
    }
    free(trocas);
  }

  return 0;
}
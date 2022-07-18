"""
  Produção Ótima de Ótima Vodka #1210

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1210

  Author: Elias E. S. Rodrigues
"""

def optimal_production_vodka(periodo, idade, maxima, preco, custo, venda, custos, trocas):
  """
    Calcula todas as possibilidades de troca ou manutenção durante o período
    proposto e a idade do destilador de 0 até máxima.

    Para cada (período, idade) verifica se é melhor trocar ou dar manutenção:
      trocar = preço do novo + custo da manutenção - valor da venda + custo acumulado
      manutenção = custo da manutenção + custo acumulado

    Se o valor de trocar for menor ou igual ao valor da manutenção, então é
    recomendado trocar. É adicionado no dicionário de custos e trocas os valores:
      custos[(período, idade)] = valor de trocar
      trocas[(período, idade)] = True, pq foi trocado
    Caso contrário é recomendado dar manutenção, então é armazenado apenas o
    valor da manutenção no dicionário custos, e nada no dicionário trocas.
      custos[(período, idade)] = valor da manuteção
  """
  for i in range(periodo, 0, -1):
    for j in range(maxima+1):
      op1 = preco + custo[0] - venda[j-1]
      op1 += custos[(i+1, 1)] if (i+1, 1) in custos else 0

      op2 = custo[j]
      op2 += custos[(i+1, j+1)] if (i+1, j+1) in custos else 0

      if op1 <= op2:
        custos[(i, j)] = op1
        trocas[(i, j)] = True
      else:
        custos[(i, j)] = op2

    """
      Quando o destilador chega a idade máxima, então tem que trocar
      obrigatoriamente.
    """
    op1 = preco + custo[0] - venda[j-1]
    op1 += custos[(i+1, 1)] if (i+1, 1) in custos else 0
    custos[(i, j)] = op1
    trocas[(i, j)] = 1

  """
    Verifica os valores dos períodos onde houve troca e monta
    a saída de anos. Os anos de troca são as tuplas (período, idade),
    onde o período e a idade do destilador foram trocados e que estão
    dentro do período proposto.
  """
  espaco = True
  idade_i = idade
  anos = ''
  for i in range(1, periodo+1):
    if (i, idade_i) in trocas:
      if not espaco:
        anos += ' '
      espaco = False
      anos += str(i)
      idade_i = 1
    else:
      idade_i += 1

  if espaco:
    anos = '0'

  return custos[(1, idade)], anos

if __name__ == '__main__':
  
  """ Arquivo de teste. """
  # file = open('./beecrowd_1210_teste.txt', 'r')
  # inputs = file.readlines()
  # file.close()
  # f = 0

  # file = open('./beecrowd_1210_resultado.txt', 'w')

  custo = [0 for i in range(2001)]
  venda = [0 for i in range(2001)]

  while True:
    try:
      """ Arquivo de teste. """
      # periodo, idadeI, idadeM, preco = inputs[f].split()
      # f += 1
      # dados = inputs[f].split()
      # for i in range(len(dados)):
      #   custo[i] = int(dados[i])
      # f += 1
      # dados = inputs[f].split()
      # for i in range(len(dados)):
      #   venda[i] = int(dados[i])
      # f += 1

      custos = {}
      trocas = {}

      periodo, idadeI, idadeM, preco = input().split()
      dados = input().split()
      for i in range(len(dados)):
        custo[i] = int(dados[i])
      dados = input().split()
      for i in range(len(dados)):
        venda[i] = int(dados[i])

      periodo = int(periodo)
      idade   = int(idadeI)
      maxima  = int(idadeM)
      preco   = int(preco)

      total, anos = optimal_production_vodka(periodo, idade, maxima, preco, custo, venda, custos, trocas)
      
      print(f'{total}\n{anos}')
      
      # file.write(f'{total}\n{anos}\n')

    except EOFError:
      exit()

  # file.close()

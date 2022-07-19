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
    recomendado trocar. É adicionado na lista de custos e trocas, os valores:
      custos[período, idade] = valor de trocar
      trocas[período, idade] = True, pq foi trocado
    Caso contrário é recomendado dar manutenção, então é armazenado o
    valor acumulado da manutenção na lista custos.
      custos[(período, idade)] = valor da manuteção
  """
  for i in range(periodo, 0, -1):
    for j in range(maxima+1):
      troca = preco + custo[0] - venda[j-1] + custos[i+1][1]
      manutencao = custo[j] + custos[i+1][j+1]

      if troca <= manutencao:
        custos[i][j] = troca
        trocas.append((i, j))
      else:
        custos[i][j] = manutencao

    """
      Quando o destilador chega a idade máxima, então tem que trocar
      obrigatoriamente.
    """
    troca = preco + custo[0] - venda[j-1] + custos[i+1][1]
    custos[i][j] = troca
    trocas.append((i, j))

  """
    Verifica os valores dos períodos onde houve troca e monta
    a saída de anos. Os anos de troca são as posições [período, idade],
    onde o período e a idade do destilador foram trocados e que estão
    dentro do período proposto.
  """
  idade_i = idade
  anos = []
  for i in range(1, periodo+1):
    if (i, idade_i) in trocas:
      anos.append(str(i))
      anos.append(' ')
      idade_i = 1
    else:
      idade_i += 1

  anos = ''.join(anos[0:-1]) if len(anos) != 0 else ['0', ' ']

  return custos[1][idade], anos

#   return custos[1][idade], ''.join(anos[0:-1])

if __name__ == '__main__':
  
  """ Arquivo de teste. """
  # file = open('./beecrowd_1210_teste.txt', 'r')
  # inputs = file.readlines()
  # file.close()
  # f = 0
  # file = open('./beecrowd_1210_resultado.txt', 'w')

  custos = [[0 for i in range(2001)] for j in range(2001)]

  while True:
    try:
      """ Arquivo de teste. """
      # periodo, idadeI, idadeM, preco = inputs[f].split()
      # f += 1
      # dados = inputs[f].split()
      # custo = [int(i) for i in dados]
      # custo += [0]
      # f += 1
      # dados = inputs[f].split()
      # venda = [int(i) for i in dados]
      # venda += [0]
      # f += 1

      periodo, idadeI, idadeM, preco = input().split()
      dados = input().split()
      custo = [int(i) for i in dados]
      custo.append(0)
      dados = input().split()
      venda = [int(i) for i in dados]
      venda.append(0)

      trocas = []

      total, anos = optimal_production_vodka(int(periodo), int(idadeI), int(idadeM), int(preco), custo, venda, custos, trocas)
      
      print(f'{total}\n{anos}')

      # file.write(f'{custos[1][idade]}\n{anos}\n')

    except EOFError:
      break

  # file.close()

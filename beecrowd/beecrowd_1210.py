"""
  Optimal Production of Great Vodka #1210

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1210

  Author: Elias E. S. Rodrigues
"""

custo = {}
memo = []

def optimal_production(ano, idadeI, periodo, idadeM, preco, manutencao, venda):
  print(f'Ano: {ano} Idade: {idadeI}')
  
  if ano == periodo:
    return 0

  if (ano, idadeI) in custo:
    return custo[(ano, idadeI)]

  aux = 99999
  custoTotal = optimal_production(ano+1, 1, periodo, idadeM, preco, manutencao, venda) + manutencao[0] - venda[idadeI-1] + preco
  memo.append(1)

  tipo = 'Troca'
  if ano < idadeM:
    aux = optimal_production(ano+1, idadeI+1, periodo, idadeM, preco, manutencao, venda) + manutencao[idadeI]

  if aux < custoTotal:
    custoTotal = aux
    memo.append(0)
    tipo = 'Manutenção'

  custo[(ano, idadeI)] = custoTotal
  print(f'Trocou - Ano: {ano} Idade: {idadeI} Tipo: {tipo} Custo: {custoTotal}')
  return custo[(ano, idadeI)]


if __name__ == '__main__':
  while True:
    try:
      periodo, idadeI, idadeM, preco = input().split()
      dados = input().split()
      manutencao = [int(i) for i in dados]
      dados = input().split()
      venda = [int(i) for i in dados]

      total = optimal_production(0, int(idadeI), int(periodo), int(idadeM), int(preco), manutencao, venda)

      print(f'{total}')
      print(custo)
      print(memo)
      # print(''.join(str(anos)))
    except EOFError:
      break

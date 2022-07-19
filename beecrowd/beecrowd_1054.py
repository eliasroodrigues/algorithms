"""
  Sapo Dinâmico #1054
  
  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1054

  Author: Elias E. S. Rodrigues
"""

def dynamic_frog(rocks):
  """
    Os dois sapos começam na margem esquerda do lago.
  """
  frog1 = [int(rocks[0][2:])]
  frog2 = [int(rocks[0][2:])]
  solution = []

  """
    O sapo 1 é o primeiro a pular.
  """
  turn1 = True

  for i in range(1, len(rocks)):
    curr_rock = int(rocks[i][2:])
    curr_type = rocks[i][0]

    """
      Verifica qual o próximo tipo de pedra para decidir
      o pulo dos sapos. Se for a pedra tipo 'S' somente um
      dos sapos pode pular nela. A cada pedra do tipo 'S'
      encontrada o pulo é alternado entre os sapos.
    """
    if curr_type == 'S':
      if turn1:
        jump1 = curr_rock - frog1[-1]
        frog1.append(curr_rock)
        solution.append(jump1)

        turn1 = False
      else:
        jump2 = curr_rock - frog2[-1]
        frog2.append(curr_rock)
        solution.append(jump2)

        turn1 = True
    else:
      """
        Se o tipo de pdra é 'B', então os dois sapos
        podem pular nela, não é necessário alternar o pulo.
      """
      jump1 = curr_rock - frog1[-1]
      jump2 = curr_rock - frog2[-1]
      frog1.append(curr_rock)
      frog2.append(curr_rock)
      solution.append(jump1)
      solution.append(jump2)

  """
    Retorna o maior valor do pulo encontrado. Como os sapos
    estão alternando os pulos nas pedras do tipo 'S' e pulando
    nas mesmas do tipo 'B', a maior distância do pulo que o
    sapo dará na ida e volta do lago será minimizada.
  """
  return max(solution)

if __name__ == "__main__":
  cases = int(input())

  for i in range(cases):
    maxD = input().split()[1]
    rocks = input().split()

    """
      Insere duas pedras grandes 'B', uma no começo para representar
      a margem esquerda (B-0) e outra no final da lista para representar
      a margem direita (B-maxD).
    """
    rocks.insert(0, 'B-0')
    rocks.append('B-' + maxD)

    answer = dynamic_frog(rocks)

    print(f'Case {i+1}: {answer}')

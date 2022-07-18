"""
  Strings Binárias Triple-Free #1432

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1432

  Author: Elias E. S. Rodrigues
"""

def check_triple_free(pattern, pos):
  limit = int(pos / 3)

  for i in range(1, limit+1):
    pos3 = pos - i
    pos2 = pos3 - i
    pos1 = pos2 - i
    flag = True

    """
      Verifica se uma sequência SSS forma uma triple-free.
    """
    for j in range(i):
      flag = False if pattern[pos1+j] != pattern[pos2+j] or pattern[pos2+j] != pattern[pos3+j] else True
      if not flag:
        break
    
    if flag:
      return False

  return True

"""
  Verifica de forma recursiva qual o valor que está na posição
  pos. Se for 0 ou 1 verifica se os valores de pos, pos-1, pos-2
  foram uma triple-free, se for verdade continua a recursão até que
  a posição seja igual o tamanho da sequência.

  Tem um problema de recalculo, vários valores são recalculados
  unúmeras vezes.
"""
def tf_binary_string(pattern, n, pos):
  if pos == n:
    return 1

  result = 0
  
  if pattern[pos] == '*':
    pattern[pos] = '0'
    if check_triple_free(pattern, pos+1):
      result += tf_binary_string(pattern, n, pos+1)
    
    pattern[pos] = '1'
    if check_triple_free(pattern, pos+1):
      result += tf_binary_string(pattern, n, pos+1)
    
    pattern[pos] = '*'
  else:
    if check_triple_free(pattern, pos+1):
      result += tf_binary_string(pattern, n, pos+1)

  return result

if __name__ == '__main__':
  """ Arquivo de teste. """
  # file = open('./beecrowd_1432_teste.txt', 'r')
  # inputs = file.readlines()
  # file.close()
  # file = open('./beecrowd_1432_resultado.txt', 'w')

  i = 0
  while True:
    # op = inputs[i].split()

    op = input().split()

    if op[0] == '0':
      break

    pattern = [num for num in op[1]]

    answer = tf_binary_string(pattern, int(op[0]), 0)

    # file.write(f'Case {i+1}: {answer}\n')

    print(f'Case {i+1}: {answer}')

    i += 1

  # file.close()

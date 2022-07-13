"""
  Triple-Free Binary Strings #1432

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

    for j in range(i):      
      if pattern[pos1+j] != pattern[pos2+j] or pattern[pos2+j] != pattern[pos3+j]:
        flag = False
        break

    if flag:
      return False

  return True

def tf_binary_string(pattern, n, pos):
  """
    If the position that will be checked is equal to the string
    length, return 1.
  """ 
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
  i = 0

  while True:
    op = input().split()

    # op = cases[i].split()

    if op[0] == '0':
      break

    pattern = [num for num in op[1]]

    answer = tf_binary_string(pattern, len(pattern), 0)

    print(f'Case {i}: {answer}')

    i += 1

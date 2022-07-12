"""
  Triple-Free Binary Strings

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1432

  Author: Elias E. S. Rodrigues
"""

memo = {}

def check_triple_free(pattern, pos):
  z = u = a = r = 0

  for i in pattern:
    if i == '0':
      z += 1    
    elif i == '1':
      u += 1
    else:
      a += 1
      z += 1
      u += 1

  if z == 3 or u == 3:
    r += 1
  
  if a == 3:
    r += 1
  
  return r

def binary_string(pattern, pos, result):
  print(f'Pattern: {pattern}, pos: {pos}, result: {result}')

  if len(pattern) >= 3:
    key = ''.join(pattern[:3])
    print(f'Key: {key}')
    if key in memo:
      result += memo[key]
    else:
      memo[key] = check_triple_free(pattern[:3], 0)
      result += memo[key]
    pos += 1
    return binary_string(pattern[pos:], pos, result)
  else:
    return result

if __name__ == '__main__':
  i = 1

  while True:
    op = input().split()

    if op[0] == '0':
      break

    pattern = [num for num in op[1]]

    print(f'Case {i}: {binary_string(pattern, 0, 0)}')

    print(memo)

    i += 1

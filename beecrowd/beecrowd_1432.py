"""
  Triple-Free Binary Strings

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1432

  Author: Elias Rodrigues
"""

def binary_string(pattern, pos):
  # print(f'Pattern: {pattern}, pos: {pos}')

  

  return 0

if __name__ == '__main__':
  i = 1

  while True:
    op = input().split()

    if op[0] == '0':
      break

    pattern = [num for num in op[1]]

    result = binary_string(pattern, 0)

    print(f'Case {i}: {result}')

    i += 1

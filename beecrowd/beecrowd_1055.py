"""
  Elegant Permuted Sum #1055

  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1055

  Author: Elias E. S. Rodrigues
"""

def elegant_permuted_sum(case):
  """
    Start the optimal solution with the first and last
    numbers of the sequence.
    Then create the new case without the two numbers
    removed for the initial solution.
    The current answer is the absolute value from the
    first - last number.
  """
  values = [case[0], case[-1]]
  new_case = case[1:-1]
  result = abs(values[0] - values[1])
  k = len(new_case)

  """
    While the length of the new case be greater then 0, do:
    Compare the two values in the current optimal solution
    with the first and last values from the new case, and
    choose the one that maximize the value of result:
      |values[0] - new_case[0]| or
      |values[1] - new_case[1]| or
      |values[0] - new_case[-1]| or
      |values[1] - new_case[-1]|.
    After picking the better one, change the number in the
    optimal solution according with the number picked and
    remove this number from new case.
    Sum the result from the previous comparison with the
    result.
    Repeat he loop.
  """
  while k > 0:
    maior = posV = posNC = -1

    if abs(values[0] - new_case[0]) > abs(values[1] - new_case[0]):
      if maior < abs(values[0] - new_case[0]):
        maior = abs(values[0] - new_case[0])
        posV = 0
        posNC = 0
    else:
      if maior < abs(values[1] - new_case[0]):
        maior = abs(values[1] - new_case[0])
        posV = 1
        posNC = 0

    if abs(values[0] - new_case[-1]) > abs(values[1] - new_case[-1]):
      if maior < abs(values[0] - new_case[-1]):
        maior = abs(values[0] - new_case[-1])
        posV = 0
        posNC = -1
    else:
      if maior < abs(values[1] - new_case[-1]):
        maior = abs(values[1] - new_case[-1])
        posV = 1
        posNC = -1

    result += maior
    values[posV] = new_case[posNC]
    new_case.remove(new_case[posNC])
    k = len(new_case)

  return result

if __name__ == '__main__':
  t = int(input())
  
  for i in range(t):
    """ Get the input and sort it in the non decreasing order. """
    case = input().split()
    case = [int(case[n]) for n in range(1, len(case))]
    case.sort()

    answer = elegant_permuted_sum(case)

    print(f'Case {i+1}: {answer}')

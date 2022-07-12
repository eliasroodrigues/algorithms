"""
  Dynamic Frog #1054
  
  Link: https://www.beecrowd.com.br/judge/pt/problems/view/1054

  Author: Elias E. S. Rodrigues
"""

def dynamic_frog(rocks):
  """ The two frogs starts at left side of the river.
  """
  frog1 = [int(rocks[0][2:])]
  frog2 = [int(rocks[0][2:])]
  solution = []

  """ Frog 1 is the first to go.
  """
  turn1 = True

  for i in range(1, len(rocks)):
    curr_rock = int(rocks[i][2:])
    curr_type = rocks[i][0]

    """ If the rock type is 'S' we need to alternate which frog can jump,
        in order to balance the jump distance.
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
      """ If the rock type is B, the two frogs can jump.
      """
      jump1 = curr_rock - frog1[-1]
      jump2 = curr_rock - frog2[-1]
      frog1.append(curr_rock)
      frog2.append(curr_rock)
      solution.append(jump1)
      solution.append(jump2)

  return max(solution)

if __name__ == "__main__":
  cases = int(input())

  for i in range(cases):
    maxD = input().split()[1]
    rocks = input().split()

    """ Insert two 'B' rocks, one on the left side with distance '0'
        and another at the right side with the 'maxD' distance. 
    """
    rocks.insert(0, 'B-0')
    rocks.append('B-' + maxD)

    answer = dynamic_frog(rocks)

    print(f'Case {i+1}: {answer}')

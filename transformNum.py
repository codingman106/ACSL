def transformNum(N, P, D):
  N = list(str(N))
  P = len(N) - P
  if 0 <= int(N[P]) <= 4:
    N[P] = str(int(N[P]) + D)[-1]
    for i in range(P+1, len(N)):
      N[i] = '0'
    N = int(''.join(N))
  elif 5 <= int(N[P]) <= 9:
    N[P] = str(abs(int(N[P]) - D))[0]
    for i in range(P+1, len(N)):
      N[i] = '0'
    N = int(''.join(N))
  return N


for i in range(5):
  N, P, D = [int(x) for x in input().split(' ')]
  result = transformNum(N, P, D)
  print(result)

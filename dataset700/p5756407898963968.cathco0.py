T = int(input())
for i in range(T):
  index = int(input())
  X = []
  for j in range(4):
    X.append(list(map(int, input().split())))
  x1 = X[index-1]
  index = int(input())
  X = []
  for j in range(4):
    X.append(list(map(int, input().split())))
  x2 = X[index-1]
  ans = set(x1).intersection(set(x2))
  if len(ans) == 0:
    print('Case #%i: Volunteer cheated!' % (i+1))
  elif len(ans) == 1:
    print('Case #%i: %i' % (i+1, ans.pop()))
  else:
    print('Case #%i: Bad magician!' % (i+1))

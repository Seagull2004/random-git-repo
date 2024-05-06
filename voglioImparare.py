import random

def pi():
  totPoints = 5000000
  totPointsInCircle = 0
  for i in range (1, totPoints + 1):
    x = random.uniform(0, 1)
    y = random.uniform(0, 1)
    if ((x ** 2 + y ** 2) < 1):
      totPointsInCircle += 1
  pi = (totPointsInCircle / totPoints) * 4
  return pi


print(pi())
print(pi())
print(pi())
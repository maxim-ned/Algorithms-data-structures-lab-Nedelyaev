import math
# целевая функция
def f(x):
  return 0.1*x**2-x*math.log(x)
l, r = 1, 2 # границы поиска
b = 0 # середина отрезка
shag = 0 # подсчёт итераций цикла
while r-l > 0.0001:
  shag += 1
  b = (l+r) / 2
  if f(b) < 0:
    r = b # сужение отрезка по правой стороне
  else:
    l = b # сужение отрезка по левой стороне
  print(shag, b)
print(b)

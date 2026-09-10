import math
# целевая функция
def f(x):
  return 0.1*x**2-x*math.log(x)
l, r = 1, 2 # границы поиска
b = 0 # середина отрезка
iteration = 0
# поиск корня с учётом погрешности
while r-l > 0.0001:
  iteration += 1
  b = (l+r) / 2
  # сужение отрезка в зависимости от знака функции в середине отрезка
  if f(b) < 0:
    r = b
  else:
    l = b
  print(iteration, b)
print(b)

from math import log
# целевая функция
def f(x):
  return 0.1*x**2-x*log(x)

# формула определения нового приближения корня
def xk(a, b):
  return a - (f(a)*(b-a))/(f(b)-f(a))

k = 0 # подсчёт итераций
a, b = 1, 2 # границы поиска
x = b # новое приближение корня
x_prev = 0 # старое приближение корня
while True:
  k += 1
  x_prev = x
  x = xk(a, b)
  if f(x) == 0: break
  # уменьшение отрезка поиска на основе равности знаков значения функции
  if f(x) * f(b) > 0: b = x
  else: a = x
  # проверка погрешности корня
  if k > 1 and abs(x - x_prev) <= 0.0001:
    break

print(x, k)

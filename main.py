import random

a = random.randint(3, 10)
z = 0
e = 2.71828182846

v = []
x = []
w = []

for i in range(a):
    x.append(random.uniform(0, 1))
    w.append(random.uniform(0, 1))

for i in range(a):
    v.append(x[i] * w[i])

for i in v:
    z = z + i

s: float = 1 / (1 + e ** -z)

print("El valor es", s)

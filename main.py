import random

a = random.randint(3, 10)
z = 0
e = 2.71828182846

v = []
x = []
w = []

for l in range(a):
    x.append(random.uniform(0, 1))
    w.append(random.randint(1, 10))

for i in range(a):
    v[i] = x[i] * w[i]

for j in v:
    z = z + j

print(z)
s = 1/(1 + e ** -z)
print(s)
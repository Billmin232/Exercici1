import random

a = random.randint(3, 10)
print(a)
i = 0
z = 0
e = 2.71828182846

v = []
x = []
w = []

for l in range(a):
    x.append(random.uniform(0, 1))
    w.append(random.randint(1, 10))

for t in range(a):
    print(x[t], w[t])

while i < a:
    v[i] = x[i] * w[i]
    i = i + 1

for j in v:
    z = z + j

print(z)
s = 1/(1 + e ** -z)
print(s)
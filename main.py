class Neurona:
    def __init__(self, inputs, pesos, Bias, fila):
        self.z = 0
        self.e = 2.71828182846
        self.fila = fila
        self.nimp = len(inputs)
        self.inputs = inputs
        self.pesos = pesos
        self.bias = Bias

    def Calcular(self):
        v = []

        for i in range(self.nimp):
            v.append(self.inputs[i] * self.pesos[self.fila][i])

        for i in v:
            self.z = self.z + i

        result = self.sigmoid(self.z)
        return result

    def LOL(self):
        return self.z

    def sigmoid(self, z):
        a = (1 / (1 + self.e ** -(z + self.bias[self.fila])))
        return a

LR = 0.25
Entradas1 = [0, 1]
z1 = [0] * 3
z2 = [0] * 2
W1 = [[1, 1],
      [1, 1],
      [1, 1]]

W2 = [[1, 1, 1],
      [1, 1, 1]]

Bias = [1, 1, 1]

n1 = Neurona(Entradas1, W1, Bias, 0)
a1 = n1.Calcular()
z1[0] = n1.LOL()

n2 = Neurona(Entradas1, W1, Bias, 1)
a2 = n2.Calcular()
z1[1] = n2.LOL()

n3 = Neurona(Entradas1, W1, Bias, 2)
a3 = n3.Calcular()
z1[2] = n3.LOL()

Entradas2 = [a1, a2, a3]
n4 = Neurona(Entradas2, W2, Bias, 0)
a4 = n4.Calcular()
z2[0] = n4.LOL()

n5 = Neurona(Entradas2, W2, Bias, 1)
a5 = n5.Calcular()
z2[1] = n5.LOL()

Salidas = [a4, a5]

Salida = [1, 0]
Err2 = [a4 - Salida[0], a5 - Salida[1]]

for i in range(2):
    for j in range(3):
        W2[i][j] = W2[i][j] - LR * (-Err2[i] * Salidas[i])

for fila in W2:
    for elemento in fila:
        print(elemento, end=' ')
    print()

import numpy as np


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

        self.z[0] = self.z[0] + self.bias[self.fila][0]
        result = self.sigmoid(self.z)
        return result

    def LOL(self):
        return self.z

    def sigmoid(self, z):
        a = (1 / (1 + np.exp(-z)))
        return a


flag = 0
LR = 0.25

#Para probar la 3a parte de la practica pon la x1 i x2 en Entradas1
Entradas1 = np.array([[1],
                      [1]])
z1 = np.array([[0],
               [0],
               [0]])
z2 = np.array([[0],
               [0]])
W1 = np.array([[1, 1],
               [1, 1],
               [1, 1]])

W2 = np.array([[1, 1, 1],
               [1, 1, 1]])

Bias1 = np.array([[1],
                  [1],
                  [1]])
Bias2 = np.array([[1],
                  [1]])

while flag != 1000:
    n1 = Neurona(Entradas1, W1, Bias1, 0)
    a1 = n1.Calcular()
    z1[0] = n1.LOL()

    n2 = Neurona(Entradas1, W1, Bias1, 1)
    a2 = n2.Calcular()
    z1[1] = n2.LOL()

    n3 = Neurona(Entradas1, W1, Bias1, 2)
    a3 = n3.Calcular()
    z1[2] = n3.LOL()

    Entradas2 = np.array([a1, a2, a3])
    n4 = Neurona(Entradas2, W2, Bias2, 0)
    a4 = n4.Calcular()
    z2[0] = n4.LOL()

    n5 = Neurona(Entradas2, W2, Bias2, 1)
    a5 = n5.Calcular()
    z2[1] = n5.LOL()

    Salidas = np.array([a4, a5])

    Salida_Des = np.array([[0],
                           [0]])
    if Entradas1[0] == 0 and Entradas1[1] == 0:
        Salida_Des[0] = 1
        Salida_Des[1] = 1
    if Entradas1[0] == 0 and Entradas1[1] == 1:
        Salida_Des[0] = 0
        Salida_Des[1] = 1
    if Entradas1[0] == 1 and Entradas1[1] == 0:
        Salida_Des[0] = 0
        Salida_Des[1] = 1
    if Entradas1[0] == 1 and Entradas1[1] == 1:
        Salida_Des[0] = 1
        Salida_Des[1] = 0

    Err2 = Salidas - Salida_Des
    W2 = W2 - LR * (np.dot(-Err2, np.transpose(Entradas2)))
    Bias2 = Bias2 - LR * -Err2

    Err1 = (np.dot(np.transpose(W2), -Err2)) * (Entradas2 * (1 - Entradas2))
    W1 = W1 - LR * np.dot(Err1, np.transpose(Entradas1))
    Bias1 = Bias1 - LR * Err1

    flag += 1

print(Salidas)

class Neurona:
    def __init__(self, inputs):
        self.z = 0
        self.e = 2.71828182846
        self.nimp = len(inputs)
        self.imputs = inputs
        self.pesos = [1] * self.nimp

    def Calcular(self):
        v = []
        self.pesos = [1] * self.nimp

        for i in range(self.nimp):
            v.append(self.imputs[i] * self.pesos[i])

        for i in v:
            self.z = self.z + i

        result = self.sigmoid(self.z)
        return result

    def sigmoid(self, z):
        a = 1 / (1 + self.e ** -(z + 1))
        return a


Entradas1 = [0, 1]
n1 = Neurona(Entradas1)
res1 = n1.Calcular()

n2 = Neurona(Entradas1)
res2 = n2.Calcular()

n3 = Neurona(Entradas1)
res3 = n3.Calcular()

Entradas2 = [res1, res2, res3]
n4 = Neurona(Entradas2)
res4 = n4.Calcular()

n5 = Neurona(Entradas2)
res5 = n5.Calcular()
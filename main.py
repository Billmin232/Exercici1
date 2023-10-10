class Neurona:
    def __init__(self, imputs):
        self.z = 0
        self.e = 2.71828182846
        self.nimp = len(imputs)
        self.imputs = imputs
        self.pesos = [1] * self.nimp

    def calcular(self):
        v = []
        self.pesos = [1] * self.nimp

        for i in range(self.nimp):
            v.append(self.imputs[i] * self.pesos[i])

        for i in v:
            self.z = self.z + i

        result = self.sigmoide(self.z)
        return result

    def sigmoide(self, z):
        a = 1 / (1 + self.e ** -(z + 1))
        return a

Entradas1 = [0,1]
n1 = Neurona(Entradas1)
res1 = n1.calcular()

n2 = Neurona(Entradas1)
res2 = n2.calcular()

n3 = Neurona(Entradas1)
res3 = n3.calcular()

Entradas2 = [res1, res2, res3]
n4 = Neurona(Entradas2)
res4 = n4.calcular()
res4 = f"{res4:.3f}"

n5 = Neurona(Entradas2)
res5 = n5.calcular()
res5 = f"{res5:.3f}"

resultados = [res4, res5]
print(resultados)
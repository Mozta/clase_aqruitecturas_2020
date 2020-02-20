import random

print("Pi�as y manzanas\n")

w = []
e = 0

for i in range (3):
    r = random.random()
    w.append(r)

x = [[1.5, -0.3, 1],
[0.9, 0.05, 1],
[2.1, 0.2, 1],
[0.24, -0.87, 0],
[0.45, -0.60, 0],
[0.15, -0.43, 0]]

c = 0

while c != 6:
    c = 0

    for i in range(0, len(x)):

        if x[i][0] * w[1] + x[i][1] * w[2] + w[0] >= 0:
            f = 1

        else:
            f = 0

        if f == x[i][2]:
            c = c + 1

        else:
            e = x[i][2] - f
            w[1] = w[1] + e * x[i][0]
            w[2] = w[2] + e * x[i][1]
            w[0] = w[0] + e

print("Pesos Perceptr�n:")
print(w)

print("\nClasificaci�n")

while True:
    x1 = float(input("\nValor de X1: "))
    x2 = float(input("Valor de X2: "))

    if x1 * w[1] + x2 * w[2] + w[0] >= 0:
        print("\nEs pi�a")

    else:
        print("\nEs manzana")

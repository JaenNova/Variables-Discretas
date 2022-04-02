"""La temperatura se comporta uniformemente dentro del rango de 95 a 100 grados
la ecuacion xi = 95 +5ri permite moldear el comportamiento de la variable continua que simula la
temperatura de una estufa
"""

print('ingrese los valores')
xo = float(input('valor de xo '))
k = float(input('valor de k '))
c = float(input('valor de c '))
g = float(input('valor de g '))
a = 1 + (4 * k)
m = 2 ** g
ri = 0
xi = 0
temperatura = 0
cantidad = int(input('ingrese la cantidad de numeros a generar '))
print('VARIABLES ALEATORIAS CONTINUAS USANDO DISTRIBUCION UNIFORME\n')
print("MEDICION         RI          TEMPERATURA")
for i in range(cantidad):
    xo = ((a * xo) + c) % m
    ri = xo / (m - 1)
    temperatura = 95 + (5 * ri)
    # imprimir los numeros
    print(f"{i + 1}              {round(ri, 3)}              {round(temperatura, 3)}")


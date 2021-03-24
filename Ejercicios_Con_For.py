#Ejercicio 1
for x in range(0,10,1):
    print(x)
#Ejercicio 2
for x in range(100,200,1):
    print(x)
#Ejercicio 3
for x in range(5,21,3):
    print(x)
#Ejercicio 4
n = int(input("Ingrese numero: "))
for x in range(n, n*2):
    print(x)
#Ejercicio 5 y 6
frase = input("Ingrese una frase: ").lower()
voca = []
for x in frase:
    if x == "a" and "a" not in voca:
        voca.append("a")
    if x == "e" and "e" not in voca:
        voca.append("e")
    if x == "i" and "i" not in voca:
        voca.append("i")
    if x == "o" and "o" not in voca:
        voca.append("o")
    if x == "u" and "u" not in voca:
        voca.append("u")
for y in voca:
    print(y)
#Ejercicio 7
S = 0
for x in range(0, 101, 1):
    S += x
    print(x)
print("La sumatoria total es ", S)
#Ejercicio 8
List = []
print("Ingrese los dos años")
ye1 = int(input("Año 1: "))
ye2 = int(input("Año 2: "))
List.append(ye1)
List.append(ye2)
print("Estos son los años bisiestos y multiplos de 10: ")
for x in range(int(min(List)), int(max(List))):
    if x % 10 == 0:
        if x % 4 == 0:
            if x % 100 != 0 or x %  400 == 0:
                print(x)
#Ejercicio 9
n = (int(input("Ingrese el numero a factorizar: ")))
fa = 1
for x in range(1, n+1):
    if n <= 0:
        break
    else:
        fa *=x
print("El numero factorial es ", fa)
#Ejercicio 10
print("Se hara la Sucession de Fibonacci de los 10 primeros numeros")
m, y = 0,1
for x in range(0, 11, 1):
    print(m)
    m, y = y, m + y
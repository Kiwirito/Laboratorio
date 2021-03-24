## Ejercicio 1 Bucles anidados
for i in range (1):
    print("Para las vocales estan estan:")
    for j in ["A", "E", "I", "O", "U"]:
        print(j)

x = input("Ahora elija una vocal (Con Mayus) = ")
if x == "A":
    print("Escojiste la primera")
elif x == "E":
    print("Escojiste la segunda")
elif x == "I":
    print("Escojiste la tercera")
elif x == "O":
    print("Escojiste la cuarta")
elif x == "U":
    print("Escojiste la quinta")
## Ejercicio 2 Bucle Anidado
plai = "Horizon Zero Dawn"
i = 0
y = len(plai)
for i in range(y):
    print(plai[:i + 1])
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
plai = input("Ingrese una palabra= ")
i = 0
y = len(plai)
x = 1
for i in range(y):
    print(plai[:i + 1])
    for k in range(1):
        print("*"*x, "= {}".format(x))

        x += 1
print("Numero total de caracteres es = ", len(plai))

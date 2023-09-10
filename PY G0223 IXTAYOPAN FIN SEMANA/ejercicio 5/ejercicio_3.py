
""""module ejercicio_3 """

cantidad = float(input("Ingrese una cantidad: \n"))
interes = float(input("Ingresa el porcentaje de interés de 1 a 100: \n"))
if interes < 30:
    cantidad = cantidad + (cantidad*(interes/100))
    print("El precio con interés es: ", cantidad)
else:
    print("El precio total es: ", cantidad)

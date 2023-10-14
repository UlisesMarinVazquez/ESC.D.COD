

""""" module ejercicio_6 """
""" print("BIENVENIDO.\n\n")
while True:

print("El menú es: \n""1. hamburguesa \n2. papas a la francesa \n3. refresco \n4. salir")


opcion = int(input("Elige una opción: "))

if opcion == 1:
    print("1. hamburguesa")
elif opcion == 2:
    print("2. papas a la francesa")
elif opcion == 3:
    print("3. refresco")
elif opcion == 4:
    print("Salida del programa.")

op_nuevo=input("Desear eligir otra opcion: si o salir")
if op_nuevo == "salir":
    break """

print("BIENVENIDO.\n")

while True:
    print("\nEl menú es:")
    print("1. hamburguesa")
    print("2. papas a la francesa")
    print("3. refresco")
    print("4. salir\n")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print("Has seleccionado: hamburguesa")
    elif opcion == 2:
        print("Has seleccionado: papas a la francesa")
    elif opcion == 3:
        print("Has seleccionado: refresco")
    elif opcion == 4:
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

    op_nuevo = input("¿Deseas elegir otra opción? (si o salir): ")
    if op_nuevo.lower() == "salir":
        print("Hasta luego...")
        break

from modulos import funciones as f

#Variable que almacenara los valores de entrada y salida de 'dinero'.
total = 0

while True:
    print("*****Bienvenido a Cajero 1.0*****")
    print("Menu")
    print("1.-Ingresar Dinero en la cuenta")
    print("2.-Retirar Dinero en la cuenta")
    print("3.-Mostrar Dinero en la cuenta")
    print("4.-Salir")

    opcion = int(input("Selecciona la opcion: "))

    if opcion == 1:
        monto = f.ingresarDinero()
        total = total + monto
    elif opcion == 2:
        montoR = f.retirarDinero(total)
        total = total - montoR
    elif opcion == 3:
        f.mostrarDinero(total)



    seguir = input("Desea seguir en el menu? (Si/no) ")

    if seguir == 'si':
        continue
    else:
        print("Adios!")
        break







def ingresarDinero():
    monto = float(input("Ingrese el monto $: "))

    return monto

def retirarDinero(x):
    total = x
    monto = float(input("Ingrese el monto a retirar $: "))

    if monto > x:
        print("No puedes retirar esa cantidad, monto total insuficiente")
        monto = 0
    else:
        print("Monto retirado {}".format(monto))
   
    return monto

def mostrarDinero(x):

    total = x

    print(total)

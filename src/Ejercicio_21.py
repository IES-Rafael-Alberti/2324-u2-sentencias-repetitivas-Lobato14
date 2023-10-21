# Crear un programa que permita al usuario ingresar los montos de las compras de un cliente 
# (se desconoce la cantidad de datos que cargará, la cual puede cambiar en cada ejecución), 
# cortando el ingreso de datos cuando el usuario ingrese el monto 0. 
# Si ingresa un monto negativo, no se debe procesar y se debe pedir que ingrese un nuevo monto. 
# Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, 
# se le debe aplicar un 10% de descuento.

def totalMonto(compras):
    compras_validas = [compra for compra in compras if compra >= 0]
    total = sum(compras_validas)
    if total > 1000:
        descuento = total * 0.1
        total -= descuento
    return total

if __name__ == "__main__":
    # Entrada
    compras = []
    monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    # Proceso
    while monto != 0:
        if monto < 0:
            print("El monto no puede ser negativo. Se ignorará esta compra.")
        else:
            compras.append(monto)
        monto = float(input("Ingrese el monto de la compra (0 para terminar): "))
    # Salida
    total_pagar = totalMonto(compras)
    print("Total a pagar: ", round(total_pagar, 2))
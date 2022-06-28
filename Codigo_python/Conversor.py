def Conversor(tipo_pesos, valor_dolar):
    pesos = input("¿cuantos pesos" + tipo_pesos + "tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al convertor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    Conversor("Colombianos", 3875)
elif opcion == 2:
    Conversor("Argentinos", 65)
elif opcion == 3:
    Conversor("Mexicanos", 20)
else:
    print("Ingresa una opcion correcta")
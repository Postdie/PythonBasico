menu = """
Bienvenido al convertor de monedas 

1 - Pesos Colombianos
2 - Pesos Argentinos
3 - Pesos Mexicanos

Elige una opcion: """

opcion = int(input(menu))

if opcion == 1:
    pesos = input("¿cuantos pesos Colombianos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 3875
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input("¿cuantos pesos Argentinos tienes?: ")
    pesos = float(pesos)
    valor_dolar = 65
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input("¿cuantos pesos Mexicanoss tienes?: ")
    pesos = float(pesos)
    valor_dolar = 20
    dolares = pesos / valor_dolar
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")
else:
    print("Ingresa una opcion correcta")
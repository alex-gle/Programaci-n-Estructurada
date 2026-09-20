#Cajero
#Oswaldo Alejandro González Avalos, Ing. Biomédica

while True:
    try:
        SALDO = float(input("¿Cuál es el saldo de la cuenta actualmente?"))
        break
    except:
        print("Ingrese solo valores numéricos")
while True:
    try:
        MONTO_RETIRADO = float(input("¿Cuál es el monto que se ha retirado el día de hoy?"))
        break
    except:
        print("Ingrese solo valores numéricos")
while True:
    try:
        MONTO = int(input("Ingrese el monto que desea retirar: "))
        break
    except:
        print("Ingrese solo valores numéricos")

if MONTO % 50 != 0 or MONTO < 0:
    print(f"Monto inválido. Saldo restante: {SALDO}")
elif MONTO > SALDO:
    print(f"Saldo insuficiente. Saldo restante: {SALDO}")
elif MONTO + MONTO_RETIRADO > 6000:
    print(f"Límite diario excedido. Saldo restante: {SALDO}")
else:
    SALDO = SALDO - MONTO
    print(f"Entregado. Su saldo restante es: {SALDO}")
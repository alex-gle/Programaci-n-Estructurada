"""PRÁCTICA 3. CAJERO NIP
Oswaldo Alejandro González Avalos
ING Biomédica 2° Semestre"""

nip_tarjeta = 1234
intentos = 3
while intentos > 0:
    try:
        nip_tecleado = int(input("Ingrese el NIP de la tarjeta: "))
    except ValueError:
        print("Debe ingresar solo números")
        continue
    if nip_tecleado == nip_tarjeta:
        print("Acceso")
        break
    else:
        intentos -= 1
        print("NIP incorrecto, intente otra vez")
if intentos == 0:
    print("Demasiados intentos. Acceso denegado")
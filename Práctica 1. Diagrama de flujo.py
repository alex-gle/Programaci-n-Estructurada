print("Bienvenido a urgencias")
while True:
    try:
        temperatura = float(input("Ingrese la temperatura del paciente: "))
        break
    except:
        print("Error, ingrese nuevamente la temperatura:")
while True:
    try:
        spo2 = int(input("Ingrese la saturación del paciente: "))
        break
    except:
        print("Error, ingrese nuevamente la saturación: ")
while True:
    try:
        fc = int(input("Ingrese la frecuencia cardiaca del paciente: "))
        break
    except:
        print("Error, ingrese nuevamente la frecuencia cardiaca")

if spo2 < 90 or fc > 120:
    print("ROJO")
elif temperatura >= 39.0:
    print("AMARILLO")
else:
    print("VERDE")

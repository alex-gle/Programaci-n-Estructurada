print("Bienvenido a urgencias")
temperatura = float(input("Ingrese la temperatura del paciente: "))
spo2 = int(input("Ingrese la saturación del paciente: "))
fc = int(input("Ingrese la frecuencia cardiaca del paciente: "))

if spo2 < 90 or fc > 120:
    print("ROJO")
elif temperatura >= 39.0:
    print("AMARILLO")
else:
    print("VERDE")

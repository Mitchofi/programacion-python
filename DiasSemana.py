numeroDia = int(
    input("Ingrese el numero del dia de la semana en un rango de entre 1-7: "))

while numeroDia>7 or numeroDia<=0:
    print("Error ingresa un numero entre el rango de 1-7, intentalo de nuevo.")
    numeroDia = int(
    input("Ingrese el numero del dia de la semana en un rango de entre 1-7: "))

if(numeroDia == 1):
    print("lunes")

if(numeroDia == 2):
    print("martes")

if(numeroDia == 3):
    print("miercoles")

if(numeroDia == 4):
    print("jueves")

if(numeroDia == 5):
    print("viernes")

if(numeroDia == 6):
    print("sabado")

if(numeroDia == 7):
    print("domingo")

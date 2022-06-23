tituloBachiller = input("Tiene diploma (Y/N): ")
edad = int(input("Ingrese la edad del alumno: "))

if tituloBachiller.upper() == "Y" and edad >= 17:
    print("El alumno puede ingresar al programa de medicina")

else:
    print("El estudiante no puede ingresar al programa de medicina")
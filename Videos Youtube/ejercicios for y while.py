#Este sumara numero siempre que se introduzca un numero mayor que 0

suma2=[]
nume4=int(input("Ingrese un numero: "))
while nume4>0:
    suma2.extend([nume4])
    nume4=int(input("Ingrese un numero: "))

print("La sumatoria de los numero es: ",(sum(suma2)))

#Esto sumarar numeros siempre que el primer numero sea mayor que el segundo
suma=[]
num=int(input("Ingrese un numero: "))
num2=0

while num>num2:

    suma.extend([num])
    num2=num
    num=int(input("ingrese un numero: "))

print("La sumatoria de los numeros es: ",(sum(suma)))

#Crear un promgrama que muestre y sume los numeros imapr de 0 a 10
sumatoria=[]

for i in range (1,10+1,2):
    print(i)
    sumatoria.extend([i])

print("La sumatoria de los numeros imapres es: ",(sum(sumatoria)))

#Crear un programa que ingrese una contraseña, la contraseña tiene que tene mas de 8 caracte, ni espacio en blanco

errores=0
contra=input("Ingrese su Contraseña: ")
for q in contra:
    if q == " ":
        errores=errores+1
longitud=len(contra)
if (errores == 0 and longitud>=8):
    print("Su contraseña es correcta...")
else:
    print("Su contraseña tiene caracteres invalidos, intente mas tarde...")

#Crea un programa que evlaue una direecion de correo, con algunos cricterios

mail=input("Ingrese su correo eletronico: ")
fallas=0
fallas2=0

for t in mail:
    if t =="@":
        fallas=fallas+1
    elif t==".":
        fallas2=fallas2+1


if (fallas == 1 and fallas2>=1):
    print("su correo es correcto")
else:
    print("Su correo es invalido ")

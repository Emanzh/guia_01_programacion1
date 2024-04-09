#5- Leer dos números reales y mostrarlos en orden creciente.
num1 =float(input('ingrese un numero para ordenar de manera creciente: '))
num2 = float(input('ingrese otro: '))
if num1 > num2:
    print(num2,num1)
else:
    print(num1,num2)
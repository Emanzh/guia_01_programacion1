#4- Leer dos números y decir cuál es el mayor.
num1 =float(input('ingrese un numero: '))
num2 = float(input('ingrese otro: '))
if num1 > num2:
    print(num1,'es mayor que',num2)
elif num2 > num1:
    print(num2,'es mayor que',num1)
else:
     print('Los numeros son iguales')
#6- Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
num1 = float(input('ingrese un numero: '))
num2 = float(input('ingrese otro numero:'))
opc = input('digite "+" si desea sumar los numeros o "-" si desea restarlos:')
if opc == '-':
    print('el resultado de la resta es',num1-num2)    
elif opc == '+':
        print('el resultado de la suma es',num2+num1)    
else:
        print('por favor ingrese una opcion valida (+/-)')
#3- Leer un número real y emitir una leyenda informando si es mayor o igual a cero o bien es negativo (son dos opciones).
numR =float(input('ingrese un numero: '))
if numR > 0:
    print(numR, 'es mayor a 0')
elif numR < 0:
    print(numR,'es menor de 0')
else:
    print('el numero es 0')

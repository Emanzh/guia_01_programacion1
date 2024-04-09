#Resolucion de Guia N° 1 Programacion
#Cepeda Caceres Emanuel DNI 35543865

#1- Pedir dos números enteros, sumarlos y mostrar el resultado.
def sumar(numero1,numero2):
    numero1 = input('Ingrese un numero: ')
    numero2 = input('Ingrese otro numero: ')
    numero1 = int(numero1) # se puede designar un input directamente como ej: int(input())
    numero2 = int(numero2)
    print('el',numero1,'y el',numero2,'dan como resultado',numero1+numero2)


#2- Pedir tres notas, calcular el promedio y mostrarlo.
def notas(nota1,nota2,nota3):
    nota1 = float(input('Ingrese un numero: '))
    nota2 = float(input('Ingrese otro numero: '))
    nota3 = float(input('Ingrese un numero: '))
    #total =nota1+nota2+nota3(tambien se puede hacer asi y promediar el total)
    print(nota1,nota2,nota3,'el promedio es',(nota1+nota2+nota3)/3)


#3- Leer un número real y emitir una leyenda informando si es mayor o igual a cero o bien es negativo (son dos opciones).
def real(numR):    
    numR =float(input('ingrese un numero: '))
    if numR >= 0:
        print(numR, 'es mayor o igual a 0')
    else:
        print(numR,'es menor de 0')


#4- Leer dos números y decir cuál es el mayor.
def mayor(num1,num2):
    num1 =float(input('ingrese un numero: '))
    num2 = float(input('ingrese otro: '))
    if num1 > num2:
        print(num1,'es mayor que',num2)
    elif num2 > num1:
        print(num2,'es mayor que',num1)
    else:
         print('Los numeros son iguales')


#5- Leer dos números reales y mostrarlos en orden creciente.
def creciente(num1,num2):
    num1 =float(input('ingrese un numero para ordenar de manera creciente: '))
    num2 = float(input('ingrese otro: '))
    if num1 > num2:
       print(num2,num1)
    else:
      print(num1,num2)


#6- Leer dos números y luego una opción (puede ser '+' o '-'), y según la opción elegida realizar el cálculo.
def suma_o_resta(num1,num2,opc):
    num1 = float(input('ingrese un numero: '))
    num2 = float(input('ingrese otro numero:'))
    opc = input('digite "+" si desea sumar los numeros o "-" si desea restarlos:')
    if opc == '-':
        print('el resultado de la resta es',num1-num2)    
    elif opc == '+':
        print('el resultado de la suma es',num2+num1)    
    else:
        print('por favor ingrese una opcion valida (+/-)')


#7- Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
def menor_o_mayor(nombre,opc):
    nombre = input('Introduzca un Nombre: ')
    opc = input('elija una opcion "<" o ">"')
    if opc == '<':
        print(nombre,'es menor de edad')    
    elif opc == '>':
            print(nombre,'es mayor de edad')    
    else:
         print('por favor ingrese una opcion valida (</>)')  


#8- Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.
def dias_horas_minutos_segundos(segundos,dias,horas,minutos,seg):
    segundos = int(input('ingrese un numero entero: '))
    dias = segundos // 86400          #86400 segundos hay en un dia.
    horas = (segundos %86400)//3600   #3600 segundos en un dia.(el resto de los segundos calculado con los dias dan las horas)
    minutos = (segundos %3600)//60    #60 segundos en una hora.(el resto de los segudos caculado con las horas da los minutos)
    seg = (segundos %60)              #el resto de los segundos quedan como segundos.
    print('son: ',dias,'dias',horas,'horas',minutos,'minutos',seg,'segundos')


#9- Realizar un algoritmo que permita ingresar un dato numérico y determinar si es un número positivo de dos dígitos.
def positivo_de_dos_dig(num):
    num = int(input('ingrese un numero: '))
    if 9 < num <=99:
         print('el numero ',num,' tiene dos digitos y es positivo')
    else:
         print('el numero ',num,' no tiene dos digitos')


#10- Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
def carrera(nombre,carrera,ciudad,cuota):   
    nombre = input('Ingrese su nombre: ')
    carrera = input('¿cual es la carrera en la que se inscribe?: ')
    ciudad = input('¿en que localidad vive?: ')
    cuota = 7000
    if carrera == 'Electromecanica' and ciudad != 'Rio Cuarto': #como hacer para que me tome mas formas de escribir?
        cuota = cuota-(cuota*0.15)
        print('el valor de su cuota es ',cuota)
    else:
         print('su cuota es de $',cuota)
     
     

#11- El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
def descuento_pasaje(pasaje,descuento,nombre,edad):    
    pasaje = 2000
    descuento = pasaje-(pasaje*0.40)
    nombre = input('indique su nombre: ')
    edad = int(input('indique su edad: '))
    if 4<edad<11:
        print('el/la señor/a',nombre,'abonara $',descuento,'como precio final del pasaje')
    elif edad>65:
        print('el/la señor/a',nombre,'abonara por ser jubilado la suma de $',descuento,'como precio final del pasaje')
    else:
        print('el precio de su boleto es de $',pasaje)
     

#12- Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
def sueldo(dias_no_trabajados,año,sueldo,año_v):
    print('por favor indique el cuestionario siguiente:')
    dias_no_trabajados = int(input('ingrese la cantidad de dias no trabajados: '))
    año = int(input('indique el año de ingreso: '))
    sueldo = 47000
    año_v = 2024
    if dias_no_trabajados == 0 and (año_v - año)>5:
        print('su sueldo es de $',sueldo*1.30)
    else:
        print('su sueldo es de $',sueldo)



while True:
    opc = int(input('ingrese su opcion\n1-sumar 2-promedio 3-real 4-mayor 5-creciente \n6-sumar o restar 7-menor o mayor 8-segundos a dias 9-positivo de dos digitos\n10-carrera universitaria 11-descuento en colectivo 12-sueldo\n0-salir: '))
    if opc== 1:
        sumar(1,2) 
    elif opc == 2 :
        notas(1,2,3)
    elif opc == 3:
        real(1)
    elif opc == 4 :
        mayor(1,2)
    elif opc == 5 :
        creciente(1,2)
    elif opc == 6 :
        suma_o_resta(1,2,3)
    elif opc == 7 :
        menor_o_mayor(1,2)
    elif opc == 8 :
        dias_horas_minutos_segundos(1,2,3,4,5)
    elif opc == 9 :
        positivo_de_dos_dig(1)
    elif opc == 10 :
        carrera(1,2,3,4)
    elif opc == 11 :
        descuento_pasaje(1,2,3,4)
    elif opc == 12:
        sueldo(1,2,3,4)
    elif opc == 0:
        print('nos vemos pronto ....')
        break
    else:
        print('opcion invalida')



    



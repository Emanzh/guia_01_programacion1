#7- Pedir un nombre y una opción ('>' o '<') y según esta mostrar por ejemplo.: Juan es menor de edad
nombre = input('Introduzca un Nombre: ')

while True:
        opc = input('elija una opcion "<" o ">" o "x": ')
        if opc == '<':
                print(nombre,'es menor de edad')    
        elif opc == '>':
                print(nombre,'es mayor de edad') 
        elif opc== 'x':
                print('\nsaliendo del programa ...\n')
                break   
        else:
                print('por favor ingrese una opcion valida (</> o x): ') 
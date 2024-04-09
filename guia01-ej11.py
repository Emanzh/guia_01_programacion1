#11- El costo del pasaje a Córdoba es de $2000. La empresa realiza un descuento de un 40 % sobre el costo del boleto a los niños que tienen entre 5 y 10 años y a los jubilados (mayores de 65). Pedir nombre y edad y mostrar el nombre y el valor final del pasaje.
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
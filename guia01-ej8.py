#8- Pasar un período expresado en segundos a un período expresado en días, horas, minutos y segundos.
segundos = int(input('ingrese un numero entero: '))
dias = segundos // 86400          #86400 segundos hay en un dia.
horas = (segundos %86400)//3600   #3600 segundos en un dia.(el resto de los segundos calculado con los dias dan las horas)
minutos = (segundos %3600)//60    #60 segundos en una hora.(el resto de los segudos caculado con las horas da los minutos)
seg = (segundos %60)              #el resto de los segundos quedan como segundos.
print('son: ',dias,'dias',horas,'horas',minutos,'minutos',seg,'segundos')

#forma auxiliar
segundos = int(input('ingrese un numero entero: '))
dias=segundos //86400
aux=segundos-(dias*86400)
horas=aux//3600
aux2=aux-(horas*3600)
minutos=aux2//60
aux3=aux2-(minutos*60)
seg=aux3
print('son: ',dias,'dias',horas,'horas',minutos,'minutos',seg,'segundos')

#forma complicada
segundos = int(input('ingrese un numero entero: '))
dias=segundos //((60*60)*24)
segundos=segundos-(dias*((60*60)*24))
horas=segundos//(60*60)
segundos=segundos-(horas*(60*60))
minutos=segundos//60
segundos=segundos-(minutos*60)
seg=segundos
print('son: ',dias,'dias',horas,'horas',minutos,'minutos',seg,'segundos')
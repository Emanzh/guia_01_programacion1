#12- Calcular el sueldo a cobrar teniendo en cuenta que  los empleados que no han faltado y  cuya antigüedad es superior a 5 años, tienen un adicional del 30% sobre el sueldo básico ($47.000). Pedir la cantidad de días no trabajados y año de ingreso en la empresa.
print('por favor indique el cuestionario siguiente:')
dias_no_trabajados = int(input('ingrese la cantidad de dias no trabajados: '))
año = int(input('indique el año de ingreso: '))
sueldo = 47000
año_v = 2024
if dias_no_trabajados == 0 and (año_v - año)>5:
    print('su sueldo es de $',sueldo*1.30)
else:
    print('su sueldo es de $',sueldo)
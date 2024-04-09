#10- Preguntar nombre, carrera en la que se inscribe y ciudad donde vive un ingresante al Instituto. Los estudiantes de la carrera de Electromecánica y que no viven en Río Cuarto tendrán un 15% de descuento en la cuota que es de $7000. Mostrar nombre, ciudad, carrera y monto final de la cuota.
nombre = input('Ingrese su nombre: ')
carrera = input('¿cual es la carrera en la que se inscribe?: ')
ciudad = input('¿en que localidad vive?: ')
cuota = 7000
if carrera == 'Electromecanica' and ciudad != 'Rio Cuarto': #como hacer para que me tome mas formas de escribir?
     cuota = cuota-(cuota*0.15)
     print('el valor de su cuota es ',cuota)
else:
     print('su cuota es de $',cuota)
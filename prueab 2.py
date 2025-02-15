calificacion1 = 10
calificacion2 = 8
calificacion3 = 7

if calificacion1 >= calificacion2 and calificacion1 >= calificacion3:
    calificacion_mas_alta = calificacion1
elif calificacion2 >= calificacion1 and calificacion2 >= calificacion3:
    calificacion_mas_alta = calificacion2
else:
    calificacion_mas_alta = calificacion3

print("La calificación más alta es:", calificacion_mas_alta)
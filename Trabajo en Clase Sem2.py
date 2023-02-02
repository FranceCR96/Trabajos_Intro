#Trabajo 1

A=1
B=2
C=3
D=4

print("El orden inverso seria:", D , C , B , A)

#Trabajo 2.
LUSTRO=5

edad=int(input("Igrese su edad"))

edadFutura= edad+LUSTRO

Print("Dentro de 5 años tendra", edad+LUSTRO)

#Trabajo 3.

numero_del_uno_al_cinco=int(input("Escoja un numero del 1 al 5 "))
numero_del_seis_al_diez=int(input("Escoja un numero del 6 al 10 "))

(numero_del_uno_al_cinco+numero_del_seis_al_diez)*2/3

print("El resultado de la operacion es:",(numero_del_uno_al_cinco+numero_del_seis_al_diez)*2/3 )

#Trabajo 4.

valorSolicitado=int(input("Escoja un numero del 1 al 99 "))

E=valorSolicitado**2
F=valorSolicitado**3

print ("El resultado del numero elevado al cuadrado seria: ", E) 
print ("El resusltado del numero elevado al cubo seria: " , F)

#Trabajo 5.

BaseRectangulo=float(input("La Base del rectangulo es: "))
AlturaRectangulo=float(input("La Altura del rectangulo es: "))
AreaRectangulo=BaseRectangulo*AlturaRectangulo
PerimetroRectangulo=2*BaseRectangulo+2*AlturaRectangulo

print("El area del rectangunlo seria: ",AreaRectangulo)
print("y el perimetro del rectangulo seria: ",PerimetroRectangulo)

#Trabajo 6.

Cuatri=15 #semanas
IdayVuelta=2
DistanciaCasaU=float(input("Indique la distancia de su Casa a la universidad "))
CostoPorKm=float(input("Indique el costo de su ida a la universidad por Km "))
DiasDeU=float(input("Indique la cantidad de dias que visita la universidad por semana "))

CostoTotal=DistanciaCasaU*CostoPorKm*DiasDeU*Cuatri*IdayVuelta

print("El gasto total de ir a la universidad",DiasDeU,"dia(s) ida y vuelta a la semana en un cuatrimestre, es de: ",CostoTotal,"colones.")

#Trabajo 7.

print("Coloca la edad de 5 personas para sacar un promedio de edades")
EdadA=int(input()) 
EdadB=int(input())
EdadC=int(input())
EdadD=int(input())
EdadE=int(input())
Promedio=(EdadA+EdadB+EdadC+EdadD+EdadE)/5

print("El promedio de edad de las 5 personas es de ",Promedio)

#Trabajo 8.

HorasSemanales=float(input("Ingresa la cantidad de horas semanales laboradas "))
CostoLaboral=float(input("Ingresa el costo de tu hora laborada "))

SalarioMensual=(HorasSemanales*4.2)*CostoLaboral

print("Tu salario mensual neto es de",SalarioMensual,"sin deducciones")

Deduccion=((HorasSemanales*4.2)*CostoLaboral*15.5)/100

SalarioReal=SalarioMensual-Deduccion

print("Tu salario depositado total es de",SalarioReal)

#Trabajo 9.

IngresoMensual=float(input("Por Favor indique sus ingresos mensuales aca "))
GastosAlimentacion=float(input("Ingrese aqui sus gastos mensuales en alimentacion "))

GastoRubroAlimentacion=(GastosAlimentacion/IngresoMensual)*100

print("El porcentaje de Gasto de Alimentacion seria de ",GastoRubroAlimentacion,"%")

GastoOtrosRubros=100-GastoRubroAlimentacion

print("El porcentaje restante que queda disponible para otros rubros es del ",GastoOtrosRubros,"%")

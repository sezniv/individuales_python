#Importando libreria

import math #importamos libreria math

#Creando funciones

def volumenCubo():
    a = float(input("Ingrese el area del cubo: "))
    resultado = a**3
    int_resultado = int(resultado)
    return print("El volumen es: " + str(int_resultado) + " centimetros")
volumenCubo()

def volumenOctraedoRegular():
    a = float(input("Ingrese la arista: "))
    raiz_cuadrada = math.sqrt(2)
    valor_final = (raiz_cuadrada * a**3)/3
    return print("El volumen de un OctraedoRegular es: " + str(valor_final))
volumenOctraedoRegular()

def volumenTetraedroRegular():
    a = float(input("Ingrese la arista: "))
    raiz = math.sqrt(2)
    valor_final = (raiz * a**3)/12
    return print("El volumen de un volumen TetraedroRegular es :" + str(valor_final))
volumenTetraedroRegular()

def volumenEsfera():
    radio = float(input("Por favor ingrese el radio de la esfera: "))
    valor_final = (4 * math.pi * (radio**3))/3
    return print("El volumen de la esfera es: " +str(valor_final))
volumenEsfera()

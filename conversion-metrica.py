# Paso 1: Solicitar al usuario las medidas de la pieza del mueble en cms

medidas_en_cms = float(input("por favor, ingrese las medidas de la pieza del mueble (en cms): "))

# Paso 2: Convertir las medidas de céntimetros a pulgadas

medidas_en_pulgadas = medidas_en_cms / 2.54

# Paso 3: Mostrar las medidas convertidas en pulgadas al usuario

print("Las medidas en pulgadas de la pieza ingresada son: ", medidas_en_pulgadas)
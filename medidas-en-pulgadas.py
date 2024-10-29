
    # Paso 1: Solicitar al usuario las medidas

medidas_en_cms = float(input("Por favor, ingresar las medidas de la pieza del muebel en cm: "))

    # Paso 2: Convertir cm en pg

medida_en_pulgadas = medidas_en_cms / 2.54

    # Paso 3: Mostrar medidas

print("Las medidas en pulgadas de la pieza ingresada son: ", medida_en_pulgadas)
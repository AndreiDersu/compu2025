def matrixmult():
    # ===============================================
    # EJERCICIO 7: Multiplicación de 2 matrices 3x3
    # Corresponde al Inciso 12
    # ===============================================

    print("Introduzca 2 Matrizes 3x3 para multiplicarlas")
    print("(introduzcalas siguiendo el siguiente formato de coordenadas):")
    print(" [0,0], [0,1], [0,2]")
    print("Matriz = [1,0],[1,1],[1,2]")
    print(" [2,0],[2,1],[2,2]")

    # Funcion para limpiar numeros complejos si la parte imaginaria es cero
    def limpio(x):
        """Retorna la parte real si el número es complejo y la parte imaginaria es 0, de lo contrario retorna el número."""
        # Nota: Esta función fue investigada para mejorar la presentación del resultado.
        return x.real if isinstance(x, complex) and x.imag == 0 else x

    try:
        print("Definamos el valor de la Primera Matriz: Matriz A")
        
        # Lectura de la Matriz A (se usa complex() para aceptar numeros complejos o reales)
        AAA = complex(input("Introduzca el valor de la casilla [0,0]:")) 
        AAB = complex(input("Introduzca el valor de la casilla [0,1]:"))
        AAC = complex(input("Introduzca el valor de la casilla [0,2]:"))
        ABA = complex(input("Introduzca el valor de la casilla [1,0]:"))
        ABB = complex(input("Introduzca el valor de la casilla [1,1]:"))
        ABC = complex(input("Introduzca el valor de la casilla [1,2]:"))
        ACA = complex(input("Introduzca el valor de la casilla [2,0]:"))
        ACB = complex(input("Introduzca el valor de la casilla [2,1]:"))
        ACC = complex(input("Introduzca el valor de la casilla [2,2]:"))

        MatrizA = [ [AAA, AAB, AAC], [ABA, ABB, ABC], [ACA, ACB, ACC] ]

        print("Ahora definamos el valor de la Segunda Matriz: Matriz B")
        
        # Lectura de la Matriz B
        BAA = complex(input("Introduzca el valor de la casilla [0,0]:"))
        BAB = complex(input("Introduzca el valor de la casilla [0,1]:"))
        BAC = complex(input("Introduzca el valor de la casilla [0,2]:"))
        BBA = complex(input("Introduzca el valor de la casilla [1,0]:"))
        BBB = complex(input("Introduzca el valor de la casilla [1,1]:"))
        BBC = complex(input("Introduzca el valor de la casilla [1,2]:"))
        BCA = complex(input("Introduzca el valor de la casilla [2,0]:"))
        BCB = complex(input("Introduzca el valor de la casilla [2,1]:"))
        BCC = complex(input("Introduzca el valor de la casilla [2,2]:"))

        MatrizB = [ [BAA, BAB, BAC], [BBA, BBB, BBC], [BCA, BCB, BCC] ]

        print("Multiplicando ambas matrices:")
        
        # Cálculo de los 9 elementos de la Matriz C = MatrizA * MatrizB
        # Fila 0
        caa = (AAA * BAA) + (AAB * BBA) + (AAC * BCA) # C[0,0]
        cab = (AAA * BAB) + (AAB * BBB) + (AAC * BCB) # C[0,1]
        cac = (AAA * BAC) + (AAB * BBC) + (AAC * BCC) # C[0,2]
        # Fila 1
        cba = (ABA * BAA) + (ABB * BBA) + (ABC * BCA) # C[1,0]
        cbb = (ABA * BAB) + (ABB * BBB) + (ABC * BCB) # C[1,1]
        cbc = (ABA * BAC) + (ABB * BBC) + (ABC * BCC) # C[1,2]
        # Fila 2
        cca = (ACA * BAA) + (ACB * BBA) + (ACC * BCA) # C[2,0]
        ccb = (ACA * BAB) + (ACB * BBB) + (ACC * BCB) # C[2,1]
        ccc = (ACA * BAC) + (ACB * BBC) + (ACC * BCC) # C[2,2]
        
        # Construccion e impresion de la Matriz C aplicando la función limpio
        MatrizC = [ [limpio(caa), limpio(cab), limpio(cac)],
                    [limpio(cba), limpio(cbb), limpio(cbc)],
                    [limpio(cca), limpio(ccb), limpio(ccc)] ]
        
        print(MatrizC)

    except ValueError:
        print("ERROR: Se introdujo un valor no valido")
    except Exception as e:
        print("Error inesperado:", e)


def matrixinv():
    # ===============================================
    # EJERCICIO 8: Inversa de una matriz 3x3
    # Corresponde al inciso 13
    # Método: Determinante y Matriz de Adjuntos
    # ===============================================


    print("Inversa de una matriz 3x3")
    print("(Introduce una Matriz siguiendo el siguiente formato de coordenadas):")
    print(" [0,0], [0,1], [0,2]")
    print("Matriz= [1,0],[1,1], [1,2]")
    print(" [2,0],[2,1],[2,2]")

    try:
        # Lectura de la Matriz A (se usa complex() para aceptar números complejos o reales)
        aa = complex(input("Introduzca el valor de la casilla [0,0]:"))
        ab = complex(input("Introduzca el valor de la casilla [0,1]:"))
        ac = complex(input("Introduzca el valor de la casilla [0,2]:"))
        ba = complex(input("Introduzca el valor de la casilla [1,0]:"))
        bb = complex(input("Introduzca el valor de la casilla [1,1]:"))
        bc = complex(input("Introduzca el valor de la casilla [1,2]:"))
        ca = complex(input("Introduzca el valor de la casilla [2,0]:"))
        cb = complex(input("Introduzca el valor de la casilla [2,1]:"))
        cc = complex(input("Introduzca el valor de la casilla [2,2]:"))

    except:
        print("Uno de los valores introducidos no es válido.")
        return

    # 1. Calculo del determinante
    determinante_de_la_matriz = aa * ((bb * cc) - (bc * cb)) - ab * ((ba * cc) - (bc * ca)) + ac * ((ba * cb) - (bb * ca))

    if determinante_de_la_matriz == 0:
        print("El determinante es 0, asi que la inversa no existe.")
        return

    # 2. Calculo de los cofactores (C)
    C11 = (bb * cc - bc * cb)
    C12 = -(ba * cc - bc * ca)
    C13 = (ba * cb - bb * ca)
    C21 = -(ab * cc - ac * cb)
    C22 = (aa * cc - ac * ca)
    C23 = -(aa * cb - ab * ca)
    C31 = (ab * bc - ac * bb)
    C32 = -(aa * bc - ac * ba)
    C33 = (aa * bb - ab * ba)

    # 3. Obtencion de la Matriz Adjunta (A) mediante la transpuesta de la Matriz de Cofactores
    A11 = C11
    A12 = C21 # C12 traspuesta
    A13 = C31 # C13 traspuesta
    A21 = C12 # C21 traspuesta
    A22 = C22
    A23 = C32 # C23 traspuesta
    A31 = C13 # C31 traspuesta
    A32 = C23 # C32 traspuesta
    A33 = C33

    # 4. Calculo de la Inversa: A_inversa = (1/det) * Adjunta(A)
    evil_determinante = 1 / determinante_de_la_matriz

    inversa = [
        [A11 * evil_determinante, A12 * evil_determinante, A13 * evil_determinante],
        [A21 * evil_determinante, A22 * evil_determinante, A23 * evil_determinante],
        [A31 * evil_determinante, A32 * evil_determinante, A33 * evil_determinante]
    ]

    # Definicion de la funcion limpio (incluida aquí por si el primer código se omite)
    def limpio(x): 
        """Retorna la parte real si el número es complejo y la parte imaginaria es 0, de lo contrario retorna el número."""
        return x.real if isinstance(x, complex) and x.imag == 0 else x

    # Aplicacion de la funcion limpio a todos los elementos de la matriz inversa
    inversa_limpia = [[limpio(v) for v in fila] for fila in inversa]

    print("La matriz inversa a la que ingresaste es:")
    print(inversa_limpia)
    

if __name__ == "__main__":
    while True:
        matrixmult()
        matrixinv()    
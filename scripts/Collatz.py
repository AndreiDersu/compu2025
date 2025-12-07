def collatz(
    entrada: int
    ) -> list:
    
    """calcula la sucesion de collatz de un numero natural k dado por el usuario.

    Args:
        entrada (int): k perteneciente a los naturales

    Returns:
        list: sucesion en forma a(n) de k hasta 1
    """
    
    try:
        k=int(entrada)
        #comprueba que el numero k sea natural
        if k <= 0:
            print("Error, ingresa un numero natural")
            return #k no es natural
        else:
            pass #k es natural, continua el codigo
               
               
        #donde a(n) es la sucesion
        a = [k]
        while True:
            
                #fin de la sucesion cuando a(n)=1
            if k == 1:
                break
            
                #si es par, usando % para sacar el resto de la division, divide entre 2 al termino
            elif k % 2 == 0:
                k = k / 2
                a.append(k)
                
                #si es impar, multiplica por 3 y le suma 1
            elif k % 2 == 1:
                k = 3 * k + 1
                a.append(k)
        return a    
    
    except ValueError:
        print("Error, ingresa un numero natural")
        return
    
    

if __name__ == "__main__":
    while True: 
        result = collatz(input("Ingresa un numero natural \n"))
        try:
            for i in range (0,len(result)):
                print(f"a_{i} = {result[i]}")
                
        except Exception:
            pass
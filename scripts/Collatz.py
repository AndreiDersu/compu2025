from math import *

def collatz (entrada):
    
    
    try:
        k=int(entrada)
        if k <= 0:
            print("Error, ingresa un numero natural")
            return
        else:
            pass     
               
        a = [k]
        while True:
            if k == 1:
                break
            elif k % 2 == 0:
                k = k / 2
                a.append(k)
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
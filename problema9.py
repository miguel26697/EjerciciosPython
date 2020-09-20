### juego
def main():
    x=150
    y=0
    while y <1000:
        n = int(input('Introduzca el numero : '))  
        if x < n:
            print ("el numero ingresado es mayor al de adivinar")
        elif x>n:
            print ("el numero ingresado es menor al de adivinar")
        else :
            y=1000
            print("fin del juego")
    y=+1

if __name__ == "__main__":
        main() 
        

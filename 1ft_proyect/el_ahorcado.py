#el ahorcado
import getpass

random_word = getpass.getpass("Introduce tu palabra: ")
word = random_word.casefold()
intentos = 5

print('''Bienvenido a mi programa, vamos a jugar al ahorcado.
Ingresa una letra y te saldra la cantidad de veces q se repite
Tienes 5 intentos''')
while True:
    letter = input("ingresar la letra o la palabra completa (escribe 'salir' para temrinar): ")
    letter_lower = letter.casefold()
    
    if letter_lower == "salir":
        print("GRACIAS POR USAR MI PROGRAMA :D")
        break
        
    elif letter_lower == word:
        print(f"Adivinaste Felicidades. La palabra era {word}")
        break
        
    elif letter_lower in word:
        print(word.count(letter_lower))
    else:
        intentos -= 1
        print(f"Fallaste tienes {intentos} intentos, prueba de nuevo")

        if intentos == 0:
            print("Te quedaste sin intentos")
            break
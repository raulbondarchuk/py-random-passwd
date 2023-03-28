import random

def obtenerCaracterRandom():
    #caracterRandom = random.randint(48, 122)
    caracterRandom = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return random.choice(caracterRandom)
    #return chr(caracterRandom)
    
def obtenerPasswdSecure(numCaracteres):
    resp = ""
    for x in range(numCaracteres):
        resp += obtenerCaracterRandom()
        
    return resp

def newPasswd():
    numCaracteres = 15 # Por defecto
    numCaracteresString = input("Por favor, introduce número de carácteres (12-30): ") # Introducido por usuario

    if numCaracteresString.isnumeric(): 
        numCaracteres = int(numCaracteresString)
    
    if numCaracteres >= 12:
        if numCaracteres <= 30:
            passwd = obtenerPasswdSecure(numCaracteres)

            # guardar la contraseña
            with open("passwd.txt", "w") as passFile:
                passFile.write(passwd)
            #print(passwd)
            print("La contraseña está guardada correctamente")
        else:
            print("¡La contraseña puede tener 30 o menus caracteres!")
    else:
        print("¡La contraseña puede tener 12 o más caracteres!")

def dropPasswd():
    with open("passwd.txt", "w") as passFile:
                passFile.write("")

def changePasswd():
    with open('passwd.txt', 'r') as file:
        passwdActual = file.read()
        passwdActualPrueba = input("Introduce la contraseña actual: (" + passwdActual + ")")

        if passwdActualPrueba == passwdActual:
            newPasswd = input("Introduce la contraseña nueva: ")
            if(len(newPasswd) >= 12):
                if(len(newPasswd) <= 30):
                    with open("passwd.txt", "w") as passFile:
                        passFile.write(newPasswd)
                else:
                    print("La nueva contraseña no es correcta")
            else:
                print("La nueva contraseña no es correcta")
        else:   
            print("La contraseña actual no es correcta")


def clearConsole():
    import os
    os.system('cls')

def viewPasswd():
    with open('passwd.txt', 'r') as file:
        if len(file.read()) > 0:
            passwd = file.read()
            return passwd
        else:
            return "UNDEFINED"

def main():
    exit = False
    clearConsole()
    while exit == False:

        print("- - - - - - - - - - - - - - -")
        print("1. Generar la nueva contraseña")
        print("2. Borrar la contraseña existente")
        print("3. Cambiar la contraseña existente")
        print("4. Salir del programa ")
        print("                         CONTRASEÑA VISIBLE: " + viewPasswd())
        print("- - - - - - - - - - - - - - -")

        choice = input("Introduce la opción: ")

        if choice == "1":
            newPasswd()
            clearConsole()

        elif choice == "2":
            dropPasswd()
            
            clearConsole()
        
        elif choice == "3":
            clearConsole()
            changePasswd()
        elif choice == "4":
            exit = True
            clearConsole()
        else:
            clearConsole()
            print("Has introducido la opción no existente")


if __name__ == '__main__':
    main()

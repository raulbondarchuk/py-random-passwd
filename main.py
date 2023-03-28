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
    
def main():
    numCaracteresString = input("Por favor, introduce número de carácteres (12-30): ") # Introducido por usuario
    numCaracteres = int(numCaracteresString)
    if numCaracteres >= 12:
        if numCaracteres <= 30:
            passwd = obtenerPasswdSecure(numCaracteres)
            print(passwd)
        else:
            print("¡La contraseña puede tener 30 o menus caracteres!")
    else:
            print("¡La contraseña puede tener 12 o más caracteres")
            
if __name__ == '__main__':
    main()

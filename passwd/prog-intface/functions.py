import random

def obtenerCaracterRandom():
    caracterRandom = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    return random.choice(caracterRandom)

def obtenerPasswdSecure(numCaracteres):
    resp = ""
    for x in range(numCaracteres):
        resp += obtenerCaracterRandom()
       
    return resp

def newPasswd(numCaracteresUser):

   
    numCaracteres = -1
    
    try:
        numCaracteres = int(numCaracteresUser)
    except ValueError:
        numCaracteres = -1

    if numCaracteres > 0:
        newPasswd = obtenerPasswdSecure(numCaracteres)
        
        with open("passwd.txt", "w") as passFile:
                passFile.write(newPasswd)
    


    
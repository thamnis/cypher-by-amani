# logique
def Chyffer_Logical(data,key=3,decode=False):
    crypted =""
    if decode:
        key = -key
    for letter in data.upper():
        if letter.isalpha():
            ascii_value = ord(letter) - ord("A")
            crypted_value = (ascii_value + key) % 26
            crypted += chr(crypted_value + ord("A"))
        else:
            crypted += letter
    return crypted
# saisir utilisateur
def Recup_Data():
    data = input("votre message : ")
    data = data.replace("é","e").replace("ê","e").replace("è","e").replace("î","i").replace("à","a").replace("â","a").replace("ù","u").replace("ï","i")
    options = input("Choisissez une optione :\n1.crypter\n2.decrypter\nchoix : ")
    if options == "1":
        encode = Chyffer_Logical(data)
        print(f"Le message crypté est : {encode}")
    elif options == "2":
        encode = Chyffer_Logical(data.capitalize())
        decode = Chyffer_Logical(encode, decode=True)
        print(f"le message decrypté est : {decode}")
    else:
        print(f"Choix indisponible") 

# Menu de lancement
def Main_Call():
    Recup_Data()
      
if __name__=='__main__':
    Main_Call()

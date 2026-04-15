# logique
def chyffer_logical(data,key=3,decode=False):
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
def recup_data():
    data = input("votre message : ")
    data = data.replace("é","e").replace("ê","e").replace("è","e").replace("î","i").replace("à","a").replace("â","a").replace("ù","u").replace("ï","i")
    options = input("Choisissez une optione :\n1.crypter\n2.decrypter\nchoix : ")
    if options == "1":
        encode = chyffer_logical(data)
        print(f"Le message crypté est : {encode}")
    elif options == "2":
        encode = chyffer_logical(data.capitalize())
        decode = chyffer_logical(encode, decode=True)
        print(f"le message decrypté est : {decode}")
    else:
        print(f"Choix indisponible") 

# Menu de lancement
def main_call():
    recup_data()
      
if __name__=='__main__':
    main_call()

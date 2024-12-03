def getDoubleAlphabet(alphabet):
    doubleAlphabet = alphabet + alphabet
    return doubleAlphabet
    
def getMessage():
    stringToEncrypt = input("Please enter a message to encrypt: ")
    return stringToEncrypt
    
def getCipherKey():
    shiftAmount = input( "Please enter a key (whole number from 1-25): ")
    return shiftAmount
    


# Función para cifrar
def encryptMessage(message, cipherKey, alphabet):
    encryptedMessage = "" # inicializamos el mensaje cifrado como vacio
    uppercaseMessage = message.upper()
    for currentCharacter in uppercaseMessage:
        # Encuentro la posición o índice en el alfabeto
        position = alphabet.find(currentCharacter)
        # Encontrar la nueva posición en el alfabeto gracias a nuestra clave
        newPosition = position + int(cipherKey)
        # Verifico el caracter exista para encriptar
        if currentCharacter in alphabet:
            encryptedMessage = encryptedMessage + alphabet[newPosition]
        else: # Si no existe el caracter se devuelve igual
            encryptedMessage = encryptedMessage + currentCharacter
    return encryptedMessage

# Desencripto utilizando la llave de forma negativa
def decryptMessage(message, cipherKey, alphabet):
    decryptKey = -1 * int(cipherKey)
    return encryptMessage(message, decryptKey, alphabet)

# Función principal
def runCaesarCipherProgram():
    # Defino el alfabeto
    myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(f'Alfabeto: {myAlphabet}')
    myAlphabet2 = getDoubleAlphabet(myAlphabet)
    print(f'Alfabeto2: {myAlphabet2}')
    # Pido el mensaje a cifrar
    myMessage = getMessage()
    print(myMessage)
    # Pido la clave
    myCipherKey = getCipherKey()
    print(myCipherKey)
    
    # Encripto
    myEncryptedMessage = encryptMessage(myMessage, myCipherKey, myAlphabet2)
    print(f'Encrypted Message: {myEncryptedMessage}')
    
    # Desencripto
    myDecryptedMessage = decryptMessage(myEncryptedMessage, myCipherKey, myAlphabet2)
    print(f'Decypted Message: {myDecryptedMessage}')


runCaesarCipherProgram()

# Defino el alfabeto
myAlphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(f'Alfabeto: {myAlphabet}')
myAlphabet2 = getDoubleAlphabet(myAlphabet)
print(f'Alfabeto2: {myAlphabet2}')
#myCipherKey = 10

for myCipherKey in range(1, 26):
    myDecryptedMessage = decryptMessage("KYWXEZS TVIWMHIRXI", myCipherKey, myAlphabet2)
    print(f'{myCipherKey} Mensaje desencriptado: {myDecryptedMessage}')
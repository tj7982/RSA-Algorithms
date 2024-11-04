
def encrypt_message(n, e, message):
    '''
    Encrypts a given message using a public key.
    :param n: part of a public key
    :param e: part of a public key
    :param message: message to be encrypted
    :return encrypted_message: a message encrypted into a list of integers, one for each
    character of the message
    '''
    encrypted_message = []
    for l in message:
        encrypted_message.append(ord(l) ** e % n)
    return encrypted_message

def main():
    n = input("Enter a value for 'n' in Hexadecimal: ")
    n = int(n, 16)
    e = input("Enter a value for 'e' in Hexadecimal: ")
    e = int(e, 16)
    message = input("Enter a string of 2-5 letters: ")
    encrypted_message = encrypt_message(n, e, message)
    print("Encrypted message: ", encrypted_message)

main()

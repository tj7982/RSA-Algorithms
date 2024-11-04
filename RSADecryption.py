
def decrypt_message(n, d, message):
    '''
    Decrypts the message by using the private key. Iterates over a list of integers representing
    the characters of the phrase, translates them to the correct ord() value, and puts them
    into a string.
    :param n: part of the private key
    :param d: part of the private key
    :param message: a list of encrypted integers representing the characters of the message
    :return decrypted_message: a string, the message decrypted using private key
    '''
    decrypted_chr = []
    decrypted_message = ""

    for v in message:
        decrypted_chr.append((int(v) ** d) % n)

    for ch in decrypted_chr:
        decrypted_message = decrypted_message + chr(ch)
    return decrypted_message

def main():
    n = input("Enter a value for 'n' in Hexadecimal: ")
    n = int(n, 16)
    d = input("Enter a value for 'd' in Hexadecimal: ")
    d = int(d, 16)
    encrypted_message = input("Enter a set of 2-5 values separated by a comma and space: ").split(', ')
    decrypted_message = decrypt_message(n, d, encrypted_message)
    print("Your decrypted message is: " + decrypted_message)

main()
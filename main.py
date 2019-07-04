string = "Tamo junto"
encrypted_string_input = "Vcoqlwpvq"
key = 2

def encrypt(string, key):
    encrypted_string_output = []
    for char in string:
        encrypted_char = chr(ord(char) + key)
        encrypted_string_output.append(encrypted_char)
    print(''.join(encrypted_string_output))



def decrypt(string, key):
    decrypted_string_output = []
    for char in encrypted_string_input:
        decrypted_char = chr(ord(char) - key)
        decrypted_string_output.append(decrypted_char)
    print(''.join(decrypted_string_output))


encrypt(string, key)
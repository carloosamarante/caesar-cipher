def encrypt(normal_string, key):
    encrypted_string_output = []
    for char in normal_string:
        encrypted_char = chr(ord(char) + key)
        encrypted_string_output.append(encrypted_char)
    print(''.join(encrypted_string_output))

def decrypt(encrypted_string, key):
    decrypted_string_output = []
    for char in encrypted_string:
        decrypted_char = chr(ord(char) - key)
        decrypted_string_output.append(decrypted_char)
    print(''.join(decrypted_string_output))

def operation_type(op, string, key):
    switcher = {
        1: encrypt,
        2: decrypt
    }
    main_function = switcher.get(op, "Invalid operation")
    return main_function(string, key)

print("Select one option bellow: (1 for Encrypt and 2 for Decrypt)")
print("1. Encrypt          2. Decrypt")
code_type = int(input())
print("Input your string:")
string = input()
print("Input the key:")
key = int(input())

operation_type(code_type, string, key)
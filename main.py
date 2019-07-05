import modules.encrypt as encrypt
import modules.decrypt as decrypt

def operation_type(op, string, key):
    switcher = {
        1: encrypt.encrypt,
        2: decrypt.decrypt
    }
    chosen_function = switcher.get(op, "Invalid operation")
    return chosen_function(string, key)

print("Select one option bellow: (1 for Encrypt and 2 for Decrypt)")
print("1. Encrypt          2. Decrypt")
code_type = int(input())
print("Input your string:")
string = input()
print("Input the key:")
key = int(input())

operation_type(code_type, string, key)
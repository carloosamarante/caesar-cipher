import modules.encrypt as encoder_model
import modules.decrypt as decoder_model

def operation_type(op, string, key):
    switcher = {
        1: encoder_model.encrypt,
        2: decoder_model.decrypt
    }
    chosen_function = switcher.get(op, "Invalid operation")
    print(chosen_function(string, key))

print("Select one option bellow: (1 for Encrypt and 2 for Decrypt)")
print("1. Encrypt          2. Decrypt")
code_type = int(input())
print("Input your string:")
string = input()
print("Input the key:")
key = int(input())

operation_type(code_type, string, key)
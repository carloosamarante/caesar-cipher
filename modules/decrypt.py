def decrypt(encrypted_string, key):
    decrypted_string_output = []
    for char in encrypted_string:
        decrypted_char = chr(ord(char) - key)
        decrypted_string_output.append(decrypted_char)
    return ''.join(decrypted_string_output)
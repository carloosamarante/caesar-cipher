def encrypt(normal_string, key):
    encrypted_string_output = []
    for char in normal_string:
        encrypted_char = chr(ord(char) + key)
        encrypted_string_output.append(encrypted_char)
    return ''.join(encrypted_string_output)
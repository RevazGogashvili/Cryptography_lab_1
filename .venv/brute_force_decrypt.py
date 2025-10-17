def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if 'a' <= char <= 'z':
            shifted_char = chr(((ord(char) - ord('a') - shift) % 26) + ord('a'))
            decrypted_text += shifted_char
        elif 'A' <= char <= 'Z':
            shifted_char = chr(((ord(char) - ord('A') - shift) % 26) + ord('A'))
            decrypted_text += shifted_char
        else:
            decrypted_text += char
    return decrypted_text


if __name__ == "__main__":
    ciphertext = "Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu."

    print(f"Ciphertext: \"{ciphertext}\"\n")
    print("--- Brute-Force Decryption ---")

    for shift_key in range(1, 26):
        plaintext = decrypt(ciphertext, shift_key)
        print(f"Shift {shift_key:2d}: {plaintext}")
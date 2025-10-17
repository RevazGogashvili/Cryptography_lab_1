import base64


def xor_decrypt(encrypted_data, key):

    decrypted_bytes = bytearray()
    key_bytes = key.encode('utf-8')
    key_len = len(key_bytes)

    for i in range(len(encrypted_data)):
        key_byte = key_bytes[i % key_len]

        decrypted_byte = encrypted_data[i] ^ key_byte

        decrypted_bytes.append(decrypted_byte)

    return decrypted_bytes


if __name__ == "__main__":
    base64_ciphertext = "Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ="
    passphrase = "SECURE"

    print("--- XOR Decryption Challenge ---")
    print(f"[*] Base64 Ciphertext: {base64_ciphertext}")
    print(f"[*] Passphrase (Key): {passphrase}\n")

    try:
        print("[1] Decoding from Base64...")
        encrypted_bytes = base64.b64decode(base64_ciphertext)
        print(f"    -> Success! Decoded {len(encrypted_bytes)} bytes of data.")

        print("[2] Performing repeating-key XOR decryption...")
        decrypted_data = xor_decrypt(encrypted_bytes, passphrase)
        print("    -> Success! Decryption complete.")

        print("[3] Decoding result into a readable string (UTF-8)...")
        final_message = decrypted_data.decode('utf-8')

        print("\n==========================================")
        print("          DECRYPTION SUCCESSFUL           ")
        print("==========================================")
        print(f"Final Message: {final_message}")
        print("==========================================")

    except base64.binascii.Error:
        print("[!] Error: The input string is not valid Base64.")
    except UnicodeDecodeError:
        print("[!] Error: Decryption failed. The resulting bytes could not be decoded.")
        print("    This usually means the wrong key was used.")
    except Exception as e:
        print(f"[!] An unexpected error occurred: {e}")
import sys

# Character set for decoding
CHARS = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ" + \
        "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~ "

# Constants decoded from the character set
PASSWORD = "g`ooxbg`mbd"  # The required password
XOR_KEY = "q`orb`kkhnm"   # The XOR decryption key

def verify_password(user_input):
    """Check if the entered password is correct"""
    if user_input == PASSWORD:
        return True
    else:
        print("That password is incorrect")
        sys.exit(0)
        return False

def decrypt_with_xor(encrypted_data, key):
    """
    Decrypt data using repeating-key XOR
    
    Args:
        encrypted_data: The encrypted bytes to decrypt
        key: The XOR key string
    
    Returns:
        The decrypted string
    """
    # Extend the key to match the length of encrypted data
    extended_key = key
    i = 0
    while len(extended_key) < len(encrypted_data):
        extended_key = extended_key + key[i]
        i = (i + 1) % len(key)
    
    # XOR each byte with the corresponding key character
    decrypted_chars = []
    for byte, key_char in zip(encrypted_data, extended_key):
        decrypted_chars.append(chr(byte ^ ord(key_char)))
    
    return ''.join(decrypted_chars)

def get_password_from_user():
    """Prompt the user for the password"""
    return input("What is the correct password for the flag?")

def read_encrypted_flag():
    """Read the encrypted flag file"""
    return open('flag.txt.enc', 'rb').read()

def print_success_message():
    """Print the success message"""
    print("Correct! Here is your flag:")

def process_flag(encrypted_flag):
    """
    Process the encrypted flag by decrypting it with XOR
    
    Args:
        encrypted_flag: The encrypted flag data (bytes)
    
    Returns:
        The decrypted flag string
    """
    # Pass bytes directly to decrypt function (don't decode first)
    return decrypt_with_xor(encrypted_flag, XOR_KEY)

def main():
    """Main program execution"""
    # Read the encrypted flag from file
    encrypted_flag = read_encrypted_flag()
    
    # Get password from user
    user_password = get_password_from_user()
    
    # Verify the password
    verify_password(user_password)
    
    # Print success message
    print_success_message()
    
    # Decrypt and display the flag
    decrypted_flag = process_flag(encrypted_flag)
    print(decrypted_flag)
    
    sys.exit(0)

if __name__ == "__main__":
    main()
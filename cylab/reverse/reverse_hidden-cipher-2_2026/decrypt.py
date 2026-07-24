#!/usr/bin/env python3
# interactive_decrypt.py

def decrypt(encoded_string, answer):
    """Decrypt encoded flag values by dividing by answer"""
    encoded_values = [int(x.strip()) for x in encoded_string.split(',')]
    return ''.join(chr(v // answer) for v in encoded_values)

def show_help():
    print("""
    =============================================
    HOW TO USE:
    1. Run the program: ./hiddencipher2
    2. Solve the math question (e.g., 4 + 5 = 9)
    3. Copy the encoded values it prints
    4. Paste them here
    5. Enter your math answer
    6. Get the flag!
    =============================================
    """)

def main():
    show_help()
    
    print("Enter the encoded values (comma-separated):")
    print("Example: 1008, 945, 891, 999, 603, 756, 630")
    encoded = input("> ").strip()
    
    print("\nEnter the answer from the math question:")
    print("Example: 9")
    try:
        answer = int(input("> ").strip())
    except ValueError:
        print("Invalid number!")
        return
    
    print("\n" + "-" * 50)
    try:
        flag = decrypt(encoded, answer)
        print(f"FLAG: {flag}")
    except Exception as e:
        print(f"Error: {e}")
        print("Make sure the encoded values are comma-separated numbers")
    print("-" * 50)

if __name__ == "__main__":
    main()
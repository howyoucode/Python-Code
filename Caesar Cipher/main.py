import string 

alphabets = string.ascii_lowercase

def encrypt(word, shift):
    encrypted = ""
    for letter in word:
        shifted = (alphabets.index(letter) + shift) % 26
        encrypted += alphabets[shifted]
    
    return encrypted

def decrypt(word, shift):
    decrypted = ""
    for letter in word:
        shifted = (alphabets.index(letter) - shift) % 26
        decrypted += alphabets[shifted]
try:
    while True:
        action = input("Do you want to encrypt or decrypt? (e/d): ").lower().strip()
        if action not in ['e', 'd']:
            print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")
            continue
        
        word = input("Enter a word: ").lower().strip()
        shift = int(input("Enter the shift number: "))
        
        if action == 'e':
            result = encrypt(word, shift)
            print(f"The encrypted word is: {result}")
        elif action == 'd':
            result = decrypt(word, shift)
            print(f"The decrypted word is: {result}")
        break
except ValueError:
    print("Invalid input. Please enter a valid word and shift number.")

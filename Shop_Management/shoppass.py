special_characters = "!@#$%^&*()-_=+[]{}\\|;:'\",.<>?/`~"
number = "0123456789"
lowercase_alphabets = "abcdefghijklmnopqrstuvwxyz"
uppercase_alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_password(password):
    check_special_Character = any(i in special_characters for i in password)
    check_number = any(i in number for i in password)
    check_uppercase = password[0] in uppercase_alphabets

    if check_number and check_special_Character and check_uppercase:
        return True
    else:
        return False

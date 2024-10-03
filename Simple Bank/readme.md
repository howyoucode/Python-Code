# Bank Account Management System

## Overview
A Python-based bank account management system that allows users to create accounts, securely log in, debit/credit amounts, and view account details. This program utilizes password validation and basic encapsulation to ensure security.

## Features
- **Create Account**: Users can create accounts with a password and initial deposit.
- **Password Validation**: The password must start with an uppercase letter, contain a special character, and a number.
- **Access Account**: Users can securely log in to their account by providing the correct account number and password.
- **Debit/Credit**: Users can debit or credit their account balance.
- **Account Details**: View current balance and account number.
- **Encapsulation**: Passwords are securely stored as private attributes and cannot be accessed directly.

## Functionality
1. **Create Account**: 
   - Enter a valid account number (6-12 digits) and a secure password.
   - Set an initial deposit.
   
2. **Access Account**:
   - Log in with your account number and password.
   - Perform debit, credit, or view account details.

3. **Debit/Credit**:
   - Debit an amount if sufficient funds are available.
   - Credit an amount to your account.

4. **Account Details**:
   - Displays the current balance and account number.

## Password Requirements
- Must start with an uppercase letter.
- Should contain at least one special character.
- Should include at least one number.

## Future Improvements
- Add secure password storage using hashing (e.g., bcrypt).
- Implement account lock after a certain number of failed login attempts.
- Add a graphical user interface (GUI) for better user interaction.

## License
This project is licensed under the MIT License.


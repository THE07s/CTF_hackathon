# Script to create bandito1 user and level environment
import os
import bandito_lib

LEVEL = 1

def main():
    # Generate level password
    user_pass = bandito_lib.get_password_hash()
    print(user_pass)

if __name__ == '__main__':
    main()
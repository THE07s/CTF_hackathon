# Script to configure bandito2 user and level environment

import os
import bandito_lib

def main():
    # Set constant for level
    LEVEL = 2

    # Add bandito2 user
    password = bandito_lib.add_user(LEVEL)

    # Configure the level, special character filename
    os.system("touch /home/bandito1/-")
    os.system(f"echo '{password}' >> /home/bandito1/-")
    os.system("chown bandito2:bandito1 /home/bandito1/-")
    os.system("chmod 640 /home/bandito1/-")

if __name__ == '__main__':
    main()
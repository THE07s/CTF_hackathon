# Script to configure bandito3 user and level environment

import os
import bandito_lib

def main():
    # Set constant for level
    LEVEL = 3

    # Add bandito3 user
    password = bandito_lib.add_user(LEVEL)

    

    # Restrict home folder access
    bandito_lib.read_only_home_folder(LEVEL)

if __name__ == '__main__':
    main()
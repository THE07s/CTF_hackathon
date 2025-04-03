# Script to configure bandito3 user and level environment

import os
import bandito_lib
import level4

def main():

    # Set constant for level
    LEVEL = 3

    # Add bandito3 user
    password = bandito_lib.add_user(LEVEL)

    # Configure the level, special character filename
    os.system("touch /home/bandito2/-")
    os.system(f"echo '{password}' >> /home/bandito2/-")
    os.system("chown bandito3:bandito2 /home/bandito2/-")
    os.system("chmod 640 /home/bandito2/-")
    
    # Restrict home folder access
    bandito_lib.read_only_home_folder(LEVEL)

    #Configure level3-4
    level4.main()

if __name__ == '__main__':
    main()
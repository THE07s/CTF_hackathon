# Script to create bandito1 user and level environment
import os
import bandito_lib



def main():
    # Set constant for level
    LEVEL = 1

    # Generate level password and create user
    password = bandito_lib.get_password_hash()
    bandito_lib.add_user(LEVEL, password)

    # Create flag readme file
    os.system("touch /home/bandito0/readme")
    os.system(f"echo '{password}' >> /home/bandito0/readme")
    os.system("chown bandito1:bandito0 /home/bandito0/readme")
    os.system("chmod 640 /home/bandito0/readme")

    # Create passfile
    bandito_lib.write_passfile(LEVEL, password)

if __name__ == '__main__':
    main()
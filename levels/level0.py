# Initial setup script for bandito0 user
import os
import bandito_lib
import level1


def main():
    # Set constant for level
    LEVEL = 0

    # Create bandito0 user and set password to bandito0
    os.system("adduser -h '/home/bandito0' -s /bin/bash -D 'bandito0' && echo 'bandito0:bandito0' | chpasswd" )

    # Write current level password to file
    bandito_lib.write_passfile(LEVEL, 'bandito0')

    # Configure Bash
    bandito_lib.configure_bashrc(LEVEL)

    # Allow SSH access
    bandito_lib.ssh_access(LEVEL)

    # Restrict home folder permisisons
    bandito_lib.read_only_home_folder(LEVEL)

    # Move on to setting up next level
    level1.main()


if __name__ == '__main__':
    main()

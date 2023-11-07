# Initial setup script for bandito0 user
import os
import hashlib
import bandito_lib
import level1

LEVEL = 0

def main():
    # Create bandito0 user and set password to bandito0
    os.system("adduser -h '/home/bandito0' -s /bin/bash -D 'bandito0' && echo 'bandito0:bandito0' | chpasswd" )

    #Allow SSH access
    bandito_lib.ssh_access(LEVEL)
    # Check correct
    os.system("cat /etc/ssh/sshd_config")

    # Move on to setting up next level
    # level1.main()
if __name__ == '__main__':
    main()

# Initial setup script for bandito0 user
import os
import hashlib

LEVEL = 0

def main():
    # Create bandito0 user and set password to bandito0
    os.system("adduser -h '/home/bandito0' -s /bin/bash -D 'bandito0' && echo 'bandito0:bandito0' | chpasswd" )

if __name__ == '__main__':
    main()

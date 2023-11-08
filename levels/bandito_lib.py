# Library to group together common functions for setting up a bandito level environment.
import os
import hashlib
from datetime import datetime


def add_user(level):
    '''Common setup for all bandito users.
    Add a user to the system and change their password.
    Write password file /etc/bandit_pass/banditX
    Configure SSH Access
    Configure Bash profile
    '''

    password = get_password_hash()
    os.system(f"adduser -h '/home/bandito{level}' -s /bin/bash -D 'bandito{level}' && echo 'bandito{level}:{password}' | chpasswd" )
    write_passfile(level, password)
    ssh_access(level)
    configure_bashrc(level)
    return password


def get_password_hash() -> str:
    '''Return MD5 hash string of current datetime YYYYMMDDHHMMSSmmm'''
    return hashlib.md5(bytes(datetime.utcnow().strftime('%Y%m%d%H%M%s%f'),
                                'utf-8')).hexdigest()


def ssh_access(level):
    '''Add user to the allowed list of SSH users'''
    os.system(f"sed -i '/^AllowUsers/ s/$/ bandito{level}/' /etc/ssh/sshd_config")


def write_passfile(level, password):
    '''Write password to /etc/bantido_pass/LEVEL and restrict permissions'''
    os.system(f'mkdir /etc/bandito_pass')
    os.system(f'touch /etc/bandito_pass/bandito{level}')
    os.system(f'echo {password} >> /etc/bandito_pass/bandito{level}')
    os.system(f'chown bandito{level}:bandito{level} /etc/bandito_pass/bandito{level}')
    os.system(f'chmod 400 /etc/bandito_pass/bandito{level}')


def configure_bashrc(level):
    '''Configure the .bashrc profile for each user'''
    # Raw string (r'') used for PS1= due to python attempting to read unicode string \u and throwing syntax error
    ps1 = "export PS1='\033[32m\033[44m\\u@\\h$ '"
    os.system(f'touch /home/bandito{level}/.bashrc')
    os.system(f'echo "{ps1}" > /home/bandito{level}/.bashrc; source ~/.bashrc')
    os.system(f'echo "{ps1}" > /home/bandito{level}/.bash_profile; source ~/.bashrc')
    os.system('clear')

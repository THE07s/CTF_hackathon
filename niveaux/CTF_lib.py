# Bibliothèque regroupant des fonctions communes pour configurer l'environnement de chaque niveau.

import os
import hashlib
from datetime import datetime, timezone


def ajout_utilisateur(niv):
    '''Configuration commune pour tous les utilisateurs de niveau.
    - Ajoute un utilisateur système et change son mot de passe.
    - Écrit le fichier de mot de passe dans /etc/niveau_mdps/niveauX.
    - Configure l'accès SSH.
    - Configure le profil Bash.
    '''
    mdp = get_mdp_hash()
    os.system(f"useradd -m -d /home/niveau{niv} -s /bin/bash niveau{niv} && echo 'niveau{niv}:{mdp}' | chpasswd")
    ecrire_fichier_mdp(niv, mdp)
    config_ssh(niv)
    config_bash(niv)
    return mdp


def get_mdp_hash() -> str:
    '''Retourne une chaîne de hachage MD5 basée sur la date actuelle au format YYYYMMDDHHMMSSmmm'''
    return hashlib.md5(bytes(datetime.now(timezone.utc).strftime('%Y%m%d%H%M%s%f'),
                                'utf-8')).hexdigest()


def config_ssh(niv):
    '''Ajoute l'utilisateur à la liste des utilisateurs autorisés pour SSH'''
    os.system(f"sed -i '/^AllowUsers/ s/$/ niveau{niv}/' /etc/ssh/sshd_config")
    os.system(f"mkdir -p /home/niveau{niv}/.ssh/")
    os.system(f"export PS1='\033[32m\033[40m\\u@\\h$; clear' > /home/niveau{niv}/.ssh/rc")
    os.system(f"echo 'source /home/niveau{niv}/.bash_profile' > /home/niveau{niv}/.ssh/rc")


def ecrire_fichier_mdp(niv, mdp):
    '''Écrit le mot de passe dans /etc/niveau_mdps/niveauX et restreint les permissions'''
    os.system(f"mkdir -p /etc/niveau_mdps")
    os.system(f"touch /etc/niveau_mdps/niveau{niv}")
    os.system(f"echo {mdp} >> /etc/niveau_mdps/niveau{niv}")
    os.system(f"chown niveau{niv}:niveau{niv} /etc/niveau_mdps/niveau{niv}")
    os.system(f"chmod 400 /etc/niveau_mdps/niveau{niv}")


def config_bash(niv):
    '''Configure les profils Bash (.bashrc et .bash_profile) pour l'utilisateur'''
    ps1 = "export PS1='\\[\\033[40m\\]\\[\\033[01;32m\\]\\u@\\h:\\[\\033[01;34m\\]\\w$ \\[\\033[40m\\]\\[\\033[00;32m\\]'"
    os.system(f"touch /home/niveau{niv}/.bashrc")
    os.system(f'echo "{ps1}" > /home/niveau{niv}/.bashrc; source /home/niveau{niv}/.bashrc')
    os.system(f"touch /home/niveau{niv}/.bash_profile")
    os.system(f'echo "{ps1}" >> /home/niveau{niv}/.bash_profile; source /home/niveau{niv}/.bash_profile')
    os.system(f'echo "alias ls=\'ls --color=never\'" >> /home/niveau{niv}/.bash_profile; source /home/niveau{niv}/.bash_profile')


def dossier_home_lecture(niv):
    '''Assure que le dossier personnel de l'utilisateur pour le niveau donné soit en lecture seule.'''
    os.system(f"chmod 500 /home/niveau{niv}")
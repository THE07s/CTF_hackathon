# Bibliothèque regroupant des fonctions communes pour configurer l'environnement de chaque niveau.

import os
import hashlib
from datetime import datetime, timezone


def ajout_utilisateur(n: int):
    username = f"niveau{n}"
    home_dir = f"/home/{username}"

    # Crée l'utilisateur avec répertoire home s'il n'existe pas
    os.system(f"id -u {username} >/dev/null 2>&1 || useradd -m -d {home_dir} -s /bin/bash {username}")

    # Crée le dossier home manuellement au cas où useradd échoue
    os.makedirs(home_dir, exist_ok=True)

    # Crée la clé SSH
    ssh_dir = f"{home_dir}/.ssh"
    os.makedirs(ssh_dir, exist_ok=True)
    os.system(f"ssh-keygen -q -t rsa -N '' -f {ssh_dir}/id_rsa <<< y >/dev/null 2>&1")
    os.system(f"cp {ssh_dir}/id_rsa.pub {ssh_dir}/authorized_keys")

    # Droits
    os.system(f"chown -R {username}:{username} {home_dir}")
    os.system(f"chmod 700 {ssh_dir}")
    os.system(f"chmod 600 {ssh_dir}/id_rsa {ssh_dir}/authorized_keys")



def get_mdp_hash(niv: int) -> str:
    '''Retourne une chaîne de hachage MD5 générée à partir d'une graine prédéfinie et du numéro de niveau.
       Ainsi, pour un même niveau, le mot de passe sera toujours identique.
    '''
    seed = "Je suis le meilleur admin de CTF !"
    data = seed + str(niv)
    return hashlib.md5(data.encode('utf-8')).hexdigest()

    # Méthode alternative basée sur le temps (à conserver en référence)
    # return hashlib.md5(bytes(datetime.now(timezone.utc).strftime('%Y%m%d%H%M%s%f'), 'utf-8')).hexdigest()


def config_ssh(niv: int):
    '''Ajoute l'utilisateur à la liste des utilisateurs autorisés pour SSH'''
    os.system(f"sed -i '/^AllowUsers/ s/$/ niveau{niv}/' /etc/ssh/sshd_config")
    os.system(f"mkdir -p /home/niveau{niv}/.ssh/")
    os.system(f"export PS1='\033[32m\033[40m\\u@\\h$; clear' > /home/niveau{niv}/.ssh/rc")
    os.system(f"echo '. /home/niveau{niv}/.bash_profile' > /home/niveau{niv}/.ssh/rc")


def ecrire_fichier_mdp(niv: int, mdp: str):
    '''Écrit le mot de passe dans /etc/niveau_mdps/niveauX et restreint les permissions'''
    os.system("mkdir -p /etc/niveau_mdps")
    os.system(f"touch /etc/niveau_mdps/niveau{niv}")
    os.system(f"echo {mdp} >> /etc/niveau_mdps/niveau{niv}")
    os.system(f"chown niveau{niv}:niveau{niv} /etc/niveau_mdps/niveau{niv}")
    os.system(f"chmod 400 /etc/niveau_mdps/niveau{niv}")


def config_bash(niv: int):
    '''Configure les profils Bash (.bashrc et .bash_profile) pour l'utilisateur'''
    ps1 = "export PS1='\\[\\033[40m\\]\\[\\033[01;32m\\]\\u@\\h:\\[\\033[01;34m\\]\\w$ \\[\\033[40m\\]\\[\\033[00;32m\\]'"
    # Redirection de l'historique dans un fichier en /tmp
    hist = "export HISTFILE=/tmp/$(whoami)_bash_history"
    os.system(f"touch /home/niveau{niv}/.bashrc")
    os.system(f'echo "{ps1}" > /home/niveau{niv}/.bashrc; echo "{hist}" >> /home/niveau{niv}/.bashrc; source /home/niveau{niv}/.bashrc')
    os.system(f"touch /home/niveau{niv}/.bash_profile")
    os.system(f'echo "{ps1}" >> /home/niveau{niv}/.bash_profile; echo "{hist}" >> /home/niveau{niv}/.bash_profile; source /home/niveau{niv}/.bash_profile')
    os.system(f'echo "alias ls=\'ls --color=never\'" >> /home/niveau{niv}/.bash_profile; source /home/niveau{niv}/.bash_profile')


def dossier_home_lecture(niv: int):
    '''Assure que le dossier personnel de l'utilisateur pour le niveau donné soit en lecture seule.'''
    os.system(f"chmod 500 /home/niveau{niv}")
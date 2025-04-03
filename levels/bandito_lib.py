import os
import hashlib
from datetime import datetime


def add_user(level, user_password=None):
    """
    Création/Configuration d'un utilisateur banditoX.
    
    Paramètres :
    - level (int) : le numéro du niveau (ex: 1 pour bandito1).
    - user_password (str, optionnel) : le mot de passe souhaité.
      - Si user_password est None, on génère un mot de passe via get_password_hash().
      - Si user_password est fourni, on l’utilise directement.
    
    Étapes :
    1) Définir le mot de passe (soit fixe, soit généré).
    2) Créer l’utilisateur banditoX et changer son mot de passe (chpasswd).
    3) Écrire le mot de passe dans /etc/bandito_pass/banditoX (fichier dont seul banditoX a la lecture).
    4) Donner l’accès SSH (ssh_access(level)).
    5) Configurer le .bashrc et le .bash_profile pour avoir un prompt coloré.
    6) Renvoyer le mot de passe (str) pour usage ultérieur.
    """

    # 1) Déterminer le mot de passe
    if user_password is None:
        # On génère un hash MD5 à partir de la date/heure
        password = get_password_hash()
    else:
        # On utilise le mot de passe fourni
        password = user_password

    # 2) Création de l’utilisateur (avec /bin/bash comme shell, home = /home/banditoX)
    #    Dans Alpine, la commande "adduser" supporte l’option -D pour "no password prompt"
    #    Sur Debian/Ubuntu, on utilise plutôt "adduser --disabled-password" ou "useradd", etc.
    #    À adapter en fonction de ta distribution. (Ici, code style Alpine)
    os.system(f"adduser -h '/home/niveau{level}' -s /bin/bash -D 'niveau{level}'")

    #    Définir (ou écraser) le mot de passe avec chpasswd
    os.system(f"echo 'niveau{level}:{password}' | chpasswd")

    # 3) Écrire le mot de passe dans /etc/bandito_pass/banditoX
    write_passfile(level, password)

    # 4) Donner l’accès SSH (ajouter 'banditoX' à la directive AllowUsers, etc.)
    ssh_access(level)

    # 5) Configurer .bashrc et .bash_profile
    configure_bashrc(level)

    # 6) Renvoyer le mot de passe pour usage ultérieur (si besoin)
    return password


def get_password_hash() -> str:
    """
    Retourne une chaîne hexadécimale MD5
    basée sur la date/heure UTC actuelle.
    
    Format de la string : YYYYMMDDHHMMss%f (microsecondes)
    - On utilise datetime.utcnow() pour la date/heure en UTC.
    - Note : %s dans strftime() est parfois non standard en Python pur,
      mais fréquemment reconnu sous Alpine ou certains environnements.
    """

    # On compose la chaîne à partir de la date/heure
    date_str = datetime.utcnow().strftime('%Y%m%d%H%M%s%f')
    # On calcule le hash MD5, puis on retourne la version hexadécimale
    return hashlib.md5(date_str.encode('utf-8')).hexdigest()


def ssh_access(level):
    """
    Ajoute l’utilisateur banditoX à la liste des utilisateurs autorisés dans /etc/ssh/sshd_config
    et configure son répertoire ~/.ssh pour personnaliser la session SSH.
    """

    # 1) sed : on va dans /etc/ssh/sshd_config, on cherche la ligne commençant par 'AllowUsers'
    #    et on ajoute " banditoX" à la fin de cette ligne.
    os.system(f"sed -i '/^AllowUsers/ s/$/ niveau{level}/' /etc/ssh/sshd_config")

    # 2) Créer le répertoire ~/.ssh/ s’il n’existe pas
    os.system(f"mkdir -p /home/niveau{level}/.ssh/")

    # 3) Configurer le fichier /home/banditoX/.ssh/rc (s’il doit être exécuté à la connexion SSH)
    #    On peut ajouter un export du PS1, faire un clear, ou sourcer le .bash_profile
    #    Exemple : on force le sourcing du .bash_profile
    os.system(f"echo 'source /home/niveau{level}/.bash_profile' > /home/niveau{level}/.ssh/rc")

    # Optionnel : ajouter d’autres configs SSH ici, définir des clés, etc.


def write_passfile(level, password):
    """
    Écrit le mot de passe dans /etc/bandito_pass/banditoX
    et applique des permissions restrictives.
    
    Étapes :
    1) Créer (si nécessaire) le répertoire /etc/bandito_pass
    2) Créer le fichier banditoX
    3) Écrire le mot de passe
    4) Changer propriétaire et permissions (400 : lecture seule pour l’utilisateur)
    """

    os.system("mkdir -p /etc/bandito_pass")
    os.system(f"touch /etc/bandito_pass/niveau{level}")
    os.system(f"echo '{password}' > /etc/bandito_pass/niveau{level}")
    os.system(f"chown niveau{level}:niveau{level} /etc/bandito_pass/niveau{level}")
    os.system(f"chmod 400 /etc/bandito_pass/niveau{level}")


def configure_bashrc(level):
    """
    Crée ou modifie les fichiers .bashrc et .bash_profile
    pour personnaliser le prompt (PS1) et ajouter un alias ls.
    """

    # Exemple de prompt coloré
    # (\u = user, \h = host, \w = répertoire courant)
    ps1 = "export PS1='\\[\\033[40m\\]\\[\\033[01;32m\\]\\u@\\h:\\[\\033[01;34m\\]\\w$ \\[\\033[40m\\]\\[\\033[00;32m\\]'"

    # On crée .bashrc et on y place la variable PS1
    os.system(f"touch /home/niveau{level}/.bashrc")
    os.system(f"echo \"{ps1}\" > /home/niveau{level}/.bashrc")

    # On crée .bash_profile et on y ajoute la même chose
    os.system(f"touch /home/niveau{level}/.bash_profile")
    os.system(f"echo \"{ps1}\" >> /home/niveau{level}/.bash_profile")

    # On ajoute un alias ls sans couleur, selon l’exemple
    os.system(f"echo \"alias ls='ls --color=never'\" >> /home/niveau{level}/.bash_profile")


def read_only_home_folder(level):
    """
    Rendre le dossier /home/banditoX non modifiable (lecture + exécution),
    donc l’utilisateur ne peut pas y écrire.
    - chmod 500 = propriétaire : rx, groupe : -, autres : -
    """
    os.system(f"chmod 500 /home/niveau{level}")

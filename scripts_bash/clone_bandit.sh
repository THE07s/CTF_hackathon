#!/bin/bash
set -e
set -o pipefail

# VÃ©rification que le script est exÃ©cutÃ© en tant que root.
if [ "$EUID" -ne 0 ]; then
    echo "Erreur : ce script doit Ãªtre exÃ©cutÃ© en tant que root." >&2
    exit 1
fi

# Fonction pour vÃ©rifier les dÃ©pendances requises.
verifier_dependances() {
    for cmd in sshpass tar rsync; do
        if ! command -v "$cmd" > /dev/null; then
            echo "Erreur : $cmd n'est pas installÃ©." >&2
            exit 1
        fi
    done
}

verifier_dependances

HOTE="bandit.labs.overthewire.org"
PORT=2220

# Liste des mots de passe pour chaque niveau.
declare -A mots_de_passe
mots_de_passe[0]="bandit0"
mots_de_passe[1]="ZjLjTmM6FvvyRnrb2rfNWOZOTa6ip5If"
mots_de_passe[2]="263JGJPfgU6LtdEvgfWU1XP5yac29mFx"
mots_de_passe[3]="MNk8KNH3Usiio41PRUEoDFPqfxLPlSmx"
mots_de_passe[4]="2WmrDFRmJIq3IPxneAaMGhap0pFhF3NJ"
mots_de_passe[5]="4oQYVPkxZOOEOO5pTW81FB8j8lxXGUQw"
mots_de_passe[6]="HWasnPhtq9AVKe0dmk45nxy20cvUa6EG"
mots_de_passe[7]="morbNTDkSW6jIlUc0ymOdMaLnOlFVAaj"
mots_de_passe[8]="dfwvzFQi4mU0wfNbFOe9RoWskMLg7eEc"
mots_de_passe[9]="4CKMh1JI91bUIZZPXDqGanal4xvAg0JM"
mots_de_passe[10]="FGUW5ilLVJrxX9kMYMmlN4MgbpfMiqey"
mots_de_passe[11]="dtR173fZKb0RRsDFSGsg2RWnpNVj3qRr"
mots_de_passe[12]="7x16WNeHIi5YkIhWsfFIqoognUTyj9Q4"
mots_de_passe[13]="FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn"
mots_de_passe[14]="MU4VWeTyJk8ROof1qqmcBPaLh7lDCPvS"
mots_de_passe[15]="8xCjnmgoKbGLhHFAZlGE5Tmu4M2tKJQo"
mots_de_passe[16]="kSkvUpMQ7lBYyCM4GBPvCvT1BfWRy0Dx"
mots_de_passe[17]="EReVavePLFHtFlFsjn3hyzMlvSuSAcRD"
mots_de_passe[18]="x2gLTTjFwMOhQ8oWNbMN362QKxfRqGlO"
mots_de_passe[19]="cGWpMaKXVwDUNgPAVJbWYuGHVn9zl3G8"
mots_de_passe[20]="0qXahG8ZjOVMN9Ghs7iOWsCfZyXOUbYO"
mots_de_passe[21]="EeoULMCra2q0dSkYj561DX7s1CpBuOBt"
mots_de_passe[22]="tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q"
mots_de_passe[23]="0Zf11ioIjMVN551jX3CmStKLYqjk54Ga"
mots_de_passe[24]="gb8KRRCsshuZXI0tUuR6ypOFjiZbf3G8"

# Fonction pour crÃ©er les utilisateurs et dÃ©finir les mots de passe.
creer_utilisateurs() {
    echo "=== CrÃ©ation des utilisateurs niveau0 Ã  niveau24 ==="
    for niveau in {0..24}; do
        utilisateur="niveau${niveau}"
        repertoire_home="/home/${utilisateur}"

        if ! id -u "$utilisateur" > /dev/null 2>&1; then
            echo "CrÃ©ation de l'utilisateur ${utilisateur} avec le rÃ©pertoire personnel ${repertoire_home}..."
            useradd -m -d "${repertoire_home}" -s /bin/bash "${utilisateur}"
        else
            echo "L'utilisateur ${utilisateur} existe dÃ©jÃ ."
        fi

        echo "${utilisateur}:${mots_de_passe[${niveau}]}" | chpasswd
        echo "Utilisateur ${utilisateur} configurÃ©."
    done
    echo "=== Tous les utilisateurs ont Ã©tÃ© crÃ©Ã©s ==="
}

# Fonction pour tÃ©lÃ©charger les niveaux et copier le contenu dans les rÃ©pertoires home.
telecharger_niveaux() {
    for niveau in {0..24}; do
        utilisateur="niveau${niveau}"
        utilisateur_distant="bandit${niveau}"
        repertoire_home="/home/${utilisateur}"
        mkdir -p "$repertoire_home"

        echo "TÃ©lÃ©chargement du niveau ${niveau} dans ${repertoire_home}..."
        max_tentatives=3
        tentative=1
        reussi=0

        while [ "$tentative" -le "$max_tentatives" ]; do
            echo "Tentative ${tentative} pour le niveau ${niveau}..."
            if sshpass -p "${mots_de_passe[$niveau]}" ssh \
                  -o StrictHostKeyChecking=no \
                  -o UserKnownHostsFile=/dev/null \
                  -o ConnectionAttempts=1 \
                  -p "$PORT" "$utilisateur_distant@$HOTE" "tar czpf - ~" | tar xzpf - -C "$repertoire_home"; then
                reussi=1
                echo "Niveau ${niveau} tÃ©lÃ©chargÃ© avec succÃ¨s lors de la tentative ${tentative}."
                break
            else
                echo "La tentative ${tentative} pour le niveau ${niveau} a Ã©chouÃ©, nouvelle tentative dans 5 secondes..."
                sleep 5
            fi
            tentative=$((tentative+1))
        done

        if [ "$reussi" -ne 1 ]; then
            echo "Impossible de tÃ©lÃ©charger le niveau ${niveau} aprÃ¨s ${max_tentatives} tentatives, passage au niveau suivant."
        fi

        # Correction des permissions pour s'assurer que le contenu appartient bien Ã  l'utilisateur.
        chown -R "$utilisateur:$utilisateur" "$repertoire_home"
        sleep 2
    done
    echo "Tous les niveaux ont Ã©tÃ© tÃ©lÃ©chargÃ©s."
}

# Flux d'exÃ©cution principal.
creer_utilisateurs
telecharger_niveaux

echo "=== Configuration terminÃ©e ! ==="

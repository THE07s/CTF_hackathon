FROM arm64v8/debian:bullseye-slim

# Définir des arguments de build pour plus de flexibilité
ARG ROOT_PASSWORD="root"

# Installer les paquets requis et nettoyer
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        tree \
        nano \
        netcat \
        telnet \
        nmap \
        openssh-server \
        openssl \
        python3 \
        python3-pip \
        bzip2 \
        vim-common \
        findutils \
        binutils \
        coreutils \
        file \
        netcat \
        tcpdump \
        iputils-ping \
        lsof \
        procps \
        build-essential \
    && rm -rf /var/lib/apt/lists/*

# Installer les dépendances Python
RUN pip3 install pandas

# Alias pour compatibilité
RUN ln -sf /bin/netcat /bin/nc || true

# Créer le répertoire de séparation des privilèges pour SSH
RUN mkdir -p /run/sshd

# Configurer SSH
RUN echo "root:${ROOT_PASSWORD}" | chpasswd && \
    sed -i 's/#Port 22/Port 2222/' /etc/ssh/sshd_config && \
    echo 'PermitRootLogin yes' >> /etc/ssh/sshd_config && \
    echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config && \
    echo 'Banner /etc/pre-auth_banner' >> /etc/ssh/sshd_config

# N'exposer que le port nécessaire
EXPOSE 22
EXPOSE 2222
EXPOSE 30000
EXPOSE 30001
EXPOSE 31000-32000


# Ajouter les personnalisations
RUN : > /etc/motd
COPY ./scripts_bash/banners.sh /etc/profile.d/
COPY scripts_bash/pre-auth_banner /etc/pre-auth_banner
RUN chmod +x /etc/profile.d/banners.sh

# Générer les clés SSH hôtes
RUN ssh-keygen -A

# Copier les fichiers de l'application
COPY ./niveaux /app

# Restreindre l'accès au code du jeu
RUN chmod -R 700 /app && chown root:root /app

# Définir le dossier de travail
WORKDIR /app

ENV LANG=C.UTF-8

# Spécifier la commande par défaut
CMD ["sh", "-c", "python3 init.py && /usr/sbin/sshd -D"]

FROM alpine:3
MAINTAINER https://github.com/rmcmillan34

# Install Bash
RUN apk add --no-cache bash

# Install and configure OpenSSH
RUN apk add --update --no-cache openssh
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config

# Add Bandito0 User
RUN adduser -h /home/bandito0 -s /bin/bash -D bindito0
RUN echo -n 'bandito0:bandito0' | chpasswd
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /
RUN chmod +x -v entrypoint.sh




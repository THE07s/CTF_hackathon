FROM alpine:3
MAINTAINER https://github.com/rmcmillan34

# Install Bash and cleanup
RUN apk update && \
  apk add --no-cache bash && \
  rm -rf /var/cache/apk/*

# Install OpenSSH and cleanup
RUN apk add --no-cache openssh
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config \
  rm -rf /var/cache/apk/*

# Configure the root user password
RUN echo 'root:B4nd1t0' | chpasswd

# Create bandito users for each level
RUN useradd -m -d /home/bandito0 -s /bin/bash bandito0 && \
  useradd -m -d /home/bandito1 -s /bin/bash bandito1 && \
  useradd -m -d /home/bandito2 -s /bin/bash bandito2 && \
  useradd -m -d /home/bandito3 -s /bin/bash bandito3 && \
  useradd -m -d /home/bandito4 -s /bin/bash bandito4 && \
  useradd -m -d /home/bandito5 -s /bin/bash bandito5 && \
  useradd -m -d /home/bandito6 -s /bin/bash bandito6 && \
  useradd -m -d /home/bandito7 -s /bin/bash bandito7 && \
  useradd -m -d /home/bandito8 -s /bin/bash bandito8 && \
  useradd -m -d /home/bandito9 -s /bin/bash bandito9 && \
  useradd -m -d /home/bandito10 -s /bin/bash bandito10 && \
  useradd -m -d /home/bandito11 -s /bin/bash bandito11 && \
  useradd -m -d /home/bandito12 -s /bin/bash bandito12 && \
  useradd -m -d /home/bandito13 -s /bin/bash bandito13 && \
  useradd -m -d /home/bandito14 -s /bin/bash bandito14 && \
  useradd -m -d /home/bandito15 -s /bin/bash bandito15 && \
  useradd -m -d /home/bandito16 -s /bin/bash bandito16 && \
  useradd -m -d /home/bandito17 -s /bin/bash bandito17 && \
  useradd -m -d /home/bandito18 -s /bin/bash bandito18 && \
  useradd -m -d /home/bandito19 -s /bin/bash bandito19 && \
  useradd -m -d /home/bandito20 -s /bin/bash bandito20 && \
  useradd -m -d /home/bandito21 -s /bin/bash bandito21 && \
  useradd -m -d /home/bandito22 -s /bin/bash bandito22 && \
  useradd -m -d /home/bandito23 -s /bin/bash bandito23 && \
  useradd -m -d /home/bandito24 -s /bin/bash bandito24 && \
  useradd -m -d /home/bandito25 -s /bin/bash bandito25 && \
  useradd -m -d /home/bandito26 -s /bin/bash bandito26 && \
  useradd -m -d /home/bandito27 -s /bin/bash bandito27 && \
  useradd -m -d /home/bandito28 -s /bin/bash bandito28 && \
  useradd -m -d /home/bandito29 -s /bin/bash bandito29 && \
  useradd -m -d /home/bandito30 -s /bin/bash bandito30 && \
  useradd -m -d /home/bandito31 -s /bin/bash bandito31 && \
  useradd -m -d /home/bandito32 -s /bin/bash bandito32 && \
  useradd -m -d /home/bandito33 -s /bin/bash bandito33 && \
  useradd -m -d /home/bandito34 -s /bin/bash bandito34

# Configure SSH for root user for administration purposes (Port 22)
RUN sed -i 's/#Port 22/Port 22/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# Configure SSH for all Bandito levels to access and play the game (Port 2222)
RUN echo 'PasswordAuthentication yes' >> /etc/ssh/sshd_config
RUN echo 'AllowUsers bandito0 bandito1 bandito2 bandito3 bandito4 bandito5 bandito6 \
  bandito7 bandito8 bandito9 bandito10 bandito11 bandito12 bandito13 bandito14 \
  bandito15 bandito16 bandito17 bandito18 bandito19 bandito20 bandito21 bandito22 \
  bandito23 bandito24 bandito25 bandito26 bandito27 bandito28 bandito29 bandito30 \
  bandito31 bandito32 bandito33 bandito34' >> /etc/ssh/sshd_config
RUN sed -i 's/#Port 2222/Port 2222/' /etc/ssh/sshd_config
  


# Add Bandito0 User
RUN adduser -h /home/bandito0 -s /bin/bash -D bandito0
RUN echo -n 'bandito0:bandito0' | chpasswd
ENTRYPOINT ["/entrypoint.sh"]
EXPOSE 22
COPY entrypoint.sh /
RUN chmod +x -v entrypoint.sh




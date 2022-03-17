FROM alpine:3

RUN apk update

RUN apk add openssh-server apache2 apache2-http2 php8 php8-apache2

# Make ssh functional
RUN ssh-keygen -A

# Make the root ssh cert folder
RUN mkdir ~/.ssh

# Allow root login
RUN sed -i 's/\#PermitRootLogin/PermitRootLogin/' /etc/ssh/sshd_config

# Allow pubkey auth
RUN sed -i 's/\#PubkeyAuthentication/PubkeyAuthentication/' /etc/ssh/sshd_config
# Disable password auth
RUN sed -i 's/\#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
# Disable Interactive auth
RUN sed -i 's/\#KbdInteractiveAuthentication yes/KbdInteractiveAuthentication no/' /etc/ssh/sshd_config

# Unlock root user
RUN passwd -u root

COPY init.sh /

RUN chmod 700 /init.sh

CMD ["/init.sh"]
apt install --yes ssh screen nano htop ranger git > /dev/null
echo "root:sahil" | chpasswd
echo "PasswordAuthentication yes" > /etc/ssh/sshd_config
echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
service ssh restart > /dev/null

wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
unzip -qq -n ngrok-stable-linux-amd64.zip

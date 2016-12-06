

# https://www.unixmen.com/install-openvpn-centos-7/

# 
yum -y install epel-release


# Step 1 — Installing OpenVPN
yum -y install openvpn

# Step 2 —  Install Easy RSA
yum -y install easy-rsa

# Step 3 — Configuring OpenVPN
cp /usr/share/doc/openvpn-*/sample/sample-config-files/server.conf  /etc/openvpn

# /etc/openvpn/server.conf
#----------------------------------------------------------------

# Change the dh file name to dh2048.pem. 
# Because the default Diffie-Hellman encryption length for Easy RSA will be 2048 bytes
# openssl dhparam -out dh2048.pem 2048
dh dh2048.pem

# uncomment the push “redirect-gateway def1 bypass-dhcp” line, 
# which tells the client to redirect all traffic through our OpenVPN.
push "redirect-gateway def1 bypass-dhcp"

# uncomment the push “dhcp-option DNS lines and updating the IP addresses.
push "dhcp-option DNS 8.8.8.8"
push "dhcp-option DNS 8.8.4.4"

# Change user and group to nobody
user nobody
group nobody











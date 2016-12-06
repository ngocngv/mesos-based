

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



# Step 4 — Generating Keys and Certificates

# Create a directory for the keys:
mkdir -p /etc/openvpn/easy-rsa/keys

# copy the key and certificate generation scripts into the directory:
cp -rf /usr/share/easy-rsa/2.0/* /etc/openvpn/easy-rsa

# edit the default values in the script. /etc/openvpn/easy-rsa/vars
# Change values that start with KEY_.
export KEY_COUNTRY="VN"
export KEY_PROVINCE="CA"
export KEY_CITY="HCM"
export KEY_ORG="FPT"
export KEY_EMAIL="info@fpt.net"
export KEY_OU="Community"
# X509 Subject Field
export KEY_NAME="vpn.fpt.net"
export KEY_CN=openvpn.fpt.net



# OpenSSL configuration may not load due to the version being undetectable. 
# To avoid this remove the version number from the openSSl file name.
cp /etc/openvpn/easy-rsa/openssl-1.0.0.cnf /etc/openvpn/easy-rsa/openssl.cnf


## To generate the keys and certificates.
source ./vars

# NOTE: If you run ./clean-all, I will be doing a rm -rf on /etc/openvpn/easy-rsa/keys
# clean up any keys and certificates which may already be in this folder and generate our certificate authority.
./clean-all 

# build the certificate authority
./build-ca

# generate the key and certificate for the server.
./build-key-server server

# generate Diffie-Hellman key exchange file.
./build-dh 


# completed the server keys and certificates generation process. 
# copy them all into our OpenVPN directory.
cd /etc/openvpn/easy-rsa/keys
cp dh2048.pem ca.crt server.crt server.key /etc/openvpn



## To have one client so we’ll just call it client.
cd /etc/openvpn/easy-rsa
./build-key client

# That's it for keys and certificates.











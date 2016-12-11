

# https://www.unixmen.com/install-openvpn-centos-7/


#--------------------------------------------------------------------------------------
# Step 6 — Configuring a Client
#--------------------------------------------------------------------------------------

# copy of the ca certificate from the server, along with the client key and certificate.
/etc/openvpn/easy-rsa/keys/ca.crt
/etc/openvpn/easy-rsa/keys/client.crt
/etc/openvpn/easy-rsa/keys/client.key



# openvon.ovpn
#--------------------------------------------------------------------
client
auth-user-pass /opt/vpn10.10/pass.txt 
dev tap8
proto udp
remote 127.0.0.1 1194
resolv-retry infinite
nobind
persist-key
persist-tun
comp-lzo
verb 3
ca ./ca.crt
cert ./client.crt
key ./client.key



# add user VPN
useradd test01
passwd test01



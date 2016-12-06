

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
dev tun
proto udp
remote your_server_ip 1194
resolv-retry infinite
nobind
persist-key
persist-tun
comp-lzo
verb 3
ca /path/to/ca.crt
cert /path/to/client.crt
key /path/to/client.key







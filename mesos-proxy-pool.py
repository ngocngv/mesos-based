

# Configuring the proxy pool


# add the Nginx repository:
yum -y install epel-release


# Installing Nginx:
yum -y install nginx

#
systemctl enable nginx
systemctl start nginx



# Installing Nixy:
# nixy - nginx auto configuration and service discovery for Mesos/Marathon

# Nixy is a daemon that automatically configures Nginx for web services deployed on Apache Mesos and Marathon.

# Features:
#----------------------------------------------------------------------------------------------------
# - Reverse proxy and load balancer for your microservices running inside Mesos and Marathon
# - Single binary with no other dependencies (except Nginx/Openresty)
# - Written in Go to be blazingly fast and concurrent.
#
# - All the features you would expect from Nginx:
#   HTTP/TCP/UDP load balancing, HTTP/2 termination, websockets, SSL/TLS termination, caching/compression, authentication, media streaming, static file serving, etc.
#
# - Zero downtime with Nginx fall-back mechanism for sick backends and hot config reload.
# - Easy to customize your needs with templating.
# - Statistics via statsd (successful/failed updates, timings).
# - Real-time updates via Marathon's event stream (Marathon v0.9.0), so no need for callbacks.
# - Support for Marathon HA cluster, auto detects sick endpoints.
# - Automatic service discovery of all running tasks inside Mesos/Marathon, including their health status.
# - Basic auth support.
# - Health checks for errors in template, nginx config or Marathon endpoints.
# - ...


#
mkdir -p /opt/nixy/
cd /opt/nixy/
#
wget https://github.com/martensson/nixy/releases/download/v0.8.0/nixy_0.8.0_linux_amd64.tar.gz
tar -xvf nixy_*.tar.gz

#
mkdir -p /opt/nixy/src/
cd /opt/nixy/src/
#
git clone https://github.com/martensson/nixy.git


# Configuring Nixy:

# vim /opt/nixy/nixy.toml
#---------------------------------------------------------------------------------------
# nixy listening port
port = "8000"
# optional X-Proxy header name
xproxy = "hostname"

# marathon api
# add all HA cluster nodes in priority order.
marathon = ["http://master-1:8080", "http://master-2:8080", "http://master-3:8080", "http://master-4:8080", "http://master-5:8080"]  

# auth
user = "" # leave empty if no auth is required.
pass = ""

# nginx
nginx_config = "/etc/nginx/nginx.conf"
nginx_template = "/opt/nixy/nginx.tmpl"
# optionally openresty
nginx_cmd = "nginx"

# statsd settings
[statsd]
addr = "localhost:8125" # optional for statistics

#namespace = "nixy.my_mesos_cluster"
#sample_rate = 100
#---------------------------------------------------------------------------------------



# vim /opt/nixy/nginx.tmpl
#---------------------------------------------------------------------------------------
# git clone https://github.com/martensson/nixy.git
cp nginx-stream.tmpl /opt/nixy/
cp nginx.tmpl /opt/nixy/




# Configure Nixy to start as a service:

# /etc/systemd/system/nixy.service:
#---------------------------------------------------------------------------------------
[Unit]  
Description=Nixy Service  
After=nginx.service

[Service]
Type=simple  
ExecStart=/bin/sh -c '/opt/nixy/nixy -f /opt/nixy/nixy.toml &> /var/log/nixy.log'  
Restart=always

[Install]
WantedBy=multi-user.target


#---------------------------------------------------------------------------------------
[Unit]  
Description=Nixy Service  
After=nginx.service

[Service]
User=root
Group=root
Type=simple  
ExecStart=/bin/sh -c '/opt/nixy/nixy -f /opt/nixy/nixy.toml &> /var/log/nixy.log'  
Restart=always

[Install]
WantedBy=multi-user.target






#
systemctl daemon-reload

systemctl enable nixy
systemctl start nixy


# Validating:
# systemctl status nixy
# tail -f /var/log/nixy.log
# URL: curl -X GET http://localhost:8000/v1/health
































































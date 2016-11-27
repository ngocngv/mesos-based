

# http://davidssysadminnotes.blogspot.com/2016/06/setting-up-haproxy-for-mesos-centos-7.html



# Setting up HAProxy for Mesos

# I wanted to use HAProxy as front end for my cluster of Mesos servers.


yum install haproxy



# /etc/haproxy/haproxy.cfg
#----------------------------------------------------------------------------

global
    log         127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

defaults
    mode                    http
    log                     global
    option                  httplog
    option                  dontlognull
    option http-server-close
    option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000

listen  stats   *:8888
        mode            http
        log             global

        maxconn 10

        clitimeout      100s
        srvtimeout      100s
        contimeout      100s
        timeout queue   100s

        stats enable
        stats hide-version
        stats refresh 30s
        stats show-node
        stats auth admin:password
        stats uri  /haproxy?stats

frontend  mesos_frontend
    bind *:80
    option http-server-close
    option forwardfor
    default_backend mesos_backend

backend mesos_backend
    balance     roundrobin
    option httpchk GET /metrics/snapshot
    http-check expect string "master\/elected":1
    server  k1 master-1:5050 check
    server  k2 master-2:5050 check
    server  k3 master-3:5050 check 

        
        
        
        
# firewall-cmd --permanent --add-port=8888/tcp
# firewall-cmd --permanent --add-port=80/tcp 
# firewall-cmd --reload



# Enable Logging

# /etc/rsyslog.conf

# Uncomment:
$ModLoad imudp
$UDPServerRun 514


# /etc/rsyslog.d/haproxy.conf
local2.* /var/log/haproxy.log


# Restart Rsyslog
systemctl restart rsyslog



# Access
# This accesses the master  
http://k1.ipaddr.com 

# The stats are here.  You'll need to supply username/password specified in config.
http://m1.ipaddr.com:8888/haproxy?stats





























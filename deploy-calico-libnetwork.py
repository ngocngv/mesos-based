

# http://docs.projectcalico.org/v2.0/getting-started/mesos/installation/docker

# Docker Configured with Cluster Store

docker daemon -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock --cluster-store=etcd://10.140.0.2:2379 --cluster-advertise=eth0:2376
            
            
            
mkdir -p /etc/systemd/system/docker.service.d/

/etc/systemd/system/docker.service.d/overlay.conf

[Service]
Environment="DOCKER_CGROUPS=--exec-opt native.cgroupdriver=systemd"
Environment="DOCKER_OPTS= --cluster-store=etcd://172.17.8.101:2379 --cluster-advertise=172.17.8.101:2380"



# mkdir -p /etc/systemd/system/docker.service.d
# /etc/systemd/system/docker.service.d/docker.conf 

# devicemapper
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --graph="/data/docker" --storage-driver=devicemapper


# docker.conf 
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --graph="/data/docker" --storage-driver=devicemapper --storage-opt dm.basesize=100G --cluster-store=etcd://172.17.8.1:2379




# After this reload daemon and restart docker service,
systemctl daemon-reload 
systemctl restart docker 



docker network create --driver calico --ipam-driver calico-ipam management-database

docker network create --driver calico --ipam-driver calico-ipam management-ui




# https://www.fusonic.net/en/blog/docker-multihost/


# etc/systemd/system/docker.service.d/30-custom.conf
[Service]
Environment="DOCKER_OPTS=--cluster-advertise eth0:2375 --cluster-store etcd://xxx.xxx.xxx.xxx:2379"

# /etc/systemd/system/docker.service.d/20-http-proxy.conf
[Service]
Environment="HTTP_PROXY=http://proxy.example.com:1234"
Environment="NO_PROXY=localhost,127.0.0.1,xxx.xxx.xxx.xxx,yyy.yyy.yyy.yyy,zzz.zzz.zzz.zzz"









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


#
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --graph="/data/docker" --storage-driver=devicemapper --storage-opt dm.basesize=100G





# After this reload daemon and restart docker service,
systemctl daemon-reload 
systemctl restart docker 



docker network create --driver calico --ipam-driver calico-ipam management-database

docker network create --driver calico --ipam-driver calico-ipam management-ui





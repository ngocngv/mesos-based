

# http://docs.projectcalico.org/v2.0/getting-started/mesos/installation/docker

# Docker Configured with Cluster Store


# mkdir -p /etc/systemd/system/docker.service.d
# 

# /etc/systemd/system/docker.service.d/10-docker-custom.conf
[Service]
ExecStart=
ExecStart=/usr/bin/dockerd --graph="/data/docker" --storage-driver=devicemapper --storage-opt dm.basesize=100G --cluster-store=etcd://127.0.0.1:2379 --cluster-advertise=em1:2377


# After this reload daemon and restart docker service,
systemctl daemon-reload 
systemctl restart docker 



docker network create --driver calico --ipam-driver calico-ipam management-database
docker network create --driver calico --ipam-driver calico-ipam management-ui




# https://www.fusonic.net/en/blog/docker-multihost/












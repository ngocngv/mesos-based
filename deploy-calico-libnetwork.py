

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





# Docker Containerizer Enabled for Mesos Agents:
echo 'docker' | tee /etc/mesos-slave/containerizers

# By default, Mesos only enables the “Mesos” Containerizer. Ensure the Docker Containerizer is also enabled on each Agent.
# systemctl restart mesos-slave




# Installing Calico
#------------------------------------------------

# Calico can be installed on each Mesos agent using the calicoctl command-line tool.

# golang calicoctl
curl -o /usr/local/bin/calicoctl -L https://github.com/projectcalico/calico-containers/releases/download/v1.0.0-beta/calicoctl
chmod +x /usr/local/bin/calicoctl

# Then, use calicoctl to launch the calico/node container:
# ETCD_ENDPOINTS=http://<ETCD_IP>:<ETCD_PORT> calicoctl node run
ETCD_ENDPOINTS=http://127.0.0.1:2379 calicoctl node run

# Running the following command:
docker run -d \
  --net=host \
  --privileged \
  --name=calico-node \
  -e IP= \
  -e IP6= \
  -e NO_DEFAULT_POOLS= \
  -e ETCD_AUTHORITY= \
  -e CALICO_LIBNETWORK_ENABLED=true \
  -e HOSTNAME=host-dc5k2u13 \
  -e CALICO_NETWORKING_BACKEND=bird \
  -e AS= \
  -e ETCD_ENDPOINTS=http://127.0.0.1:2379 \
  -e ETCD_SCHEME= \
  -v /var/log/calico:/var/log/calico \
  -v /var/run/calico:/var/run/calico \
  -v /lib/modules:/lib/modules \
  -v /run/docker/plugins:/run/docker/plugins \
  -v /var/run/docker.sock:/var/run/docker.sock \
  calico/node:v1.0.0-beta



    
    
    
    
    

docker network create --driver calico --ipam-driver calico-ipam management-database
docker network create --driver calico --ipam-driver calico-ipam management-ui




# https://www.fusonic.net/en/blog/docker-multihost/












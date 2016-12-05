

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
curl -o /usr/local/bin/calicoctl -L https://github.com/projectcalico/calico-containers/releases/download/v1.0.0-rc1/calicoctl
chmod +x /usr/local/bin/calicoctl


# Use calicoctl to launch the calico/node container:
# ETCD_ENDPOINTS=http://<ETCD_IP>:<ETCD_PORT> calicoctl node run
ETCD_ENDPOINTS=http://127.0.0.1:2379 calicoctl node run

# Running the following command:
docker run -d \
    --net=host \
    --privileged \
    --name=calico-node \
    --restart=always \
    -e NO_DEFAULT_POOLS= \
    -e CALICO_LIBNETWORK_ENABLED=true \
    -e ETCD_ENDPOINTS=http://127.0.0.1:2379 \
    -e ETCD_AUTHORITY=127.0.0.1:2379 \        
    -e ETCD_SCHEME= \
    -e NODENAME=host-dc5k2u13 \
    -e CALICO_NETWORKING_BACKEND=bird \
    -v /var/run/docker.sock:/var/run/docker.sock \
    -v /var/run/calico:/var/run/calico \
    -v /lib/modules:/lib/modules \
    -v /var/log/calico:/var/log/calico \
    -v /run/docker/plugins:/run/docker/plugins \
    calico/node:latest





# Running the Calico Node Container as a Service:
# http://docs.projectcalico.org/v2.0/usage/configuration/as-service

# set calico environment file calico.env
# /etc/calico/calico.env
# /etc/default/calico.env
#--------------------------------------------------------------
ETCD_ENDPOINTS=http://127.0.0.1:2379
ETCD_CA_FILE=""
ETCD_CERT_FILE=""
ETCD_KEY_FILE=""
CALICO_HOSTNAME="host-dc5k2u13"
CALICO_NO_DEFAULT_POOLS=""
CALICO_IP=""
CALICO_IP6=""
CALICO_AS=""
CALICO_LIBNETWORK_ENABLED=true
CALICO_NETWORKING_BACKEND=bird
ETCD_AUTHORITY=http://127.0.0.1:2379   #IP and port of etcd instance used by Calico


# Be sure to update this environment file as necessary, 
# such as modifying ETCD_ENDPOINTS to point at the correct etcd cluster endpoints.



# generate systemd unit file

# /usr/lib/systemd/system/calico.service

# /etc/systemd/system/calico-node.service
#-----------------------------------------------------------------------------
[Unit]
Description=calico-node
After=docker.service
Requires=docker.service

[Service]
EnvironmentFile=/etc/calico/calico.env
ExecStartPre=-/usr/bin/docker rm -f calico-node
ExecStart=/usr/bin/docker run --net=host --privileged \
 --name=calico-node \
 -e HOSTNAME=${HOSTNAME} \
 -e IP=${CALICO_IP} \
 -e IP6=${CALICO_IP6} \
 -e CALICO_NETWORKING_BACKEND=${CALICO_NETWORKING_BACKEND} \
 -e AS=${CALICO_AS} \
 -e NO_DEFAULT_POOLS=${CALICO_NO_DEFAULT_POOLS} \
 -e CALICO_LIBNETWORK_ENABLED=${CALICO_LIBNETWORK_ENABLED} \
 -e ETCD_ENDPOINTS=${ETCD_ENDPOINTS} \
 -e ETCD_CA_CERT_FILE=${ETCD_CA_CERT_FILE} \
 -e ETCD_CERT_FILE=${ETCD_CERT_FILE} \
 -e ETCD_KEY_FILE=${ETCD_KEY_FILE} \
 -v /var/log/calico:/var/log/calico \
 -v /run/docker/plugins:/run/docker/plugins \
 -v /lib/modules:/lib/modules \
 -v /var/run/calico:/var/run/calico \
 calico/node:v1.0.0-beta

ExecStop=-/usr/bin/docker stop calico-node

[Install]
WantedBy=multi-user.target



#-----------------------------------------------------------------------------
[Service]
Type=forking
RemainAfterExit=yes
Restart=on-failure
RestartSec=20
TimeoutStartSec=20m

ExecStartPre=-/usr/bin/docker rm -f calico-node
EnvironmentFile=/etc/default/calico
ExecStart=/usr/bin/calicoctl node --ip="private_ipv4" --node-image="calico_image:calico_image_tag"

ExecStop=/usr/bin/calicoctl node stop
ExecStopPost=-/usr/bin/docker rm -f calico-node



#-----------------------------------------------------------------------------
systemctl daemon-reload
systemctl enable calico-node
systemctl start calico-node 

#
systemctl status calico-node






#
calicoctl node status



   
    
    

docker network create --driver calico --ipam-driver calico-ipam management-database
docker network create --driver calico --ipam-driver calico-ipam management-ui




# https://www.fusonic.net/en/blog/docker-multihost/



# tshoot
systemctl status etcd
curl 127.0.0.1:2379/v2/keys







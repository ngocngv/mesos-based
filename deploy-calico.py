


# Installing Calico-CNI for the Unified Containerizer
# http://docs.projectcalico.org/v2.0/getting-started/mesos/installation/unified



# How to add Calico networking to a Mesos Agent with CNI enabled.


# Prerequisites

# When enabling CNI in Mesos, you will have specified a network_cni_config_dir and network_cni_plugins_dir. 
# We’ll refer to these going forward as $NETWORK_CNI_CONFIG_DIR and $NETWORK_CNI_PLUGINS_DIR, respectively.


# Make dirs if they don't exist
mkdir -p /var/lib/mesos/cni/plugins
mkdir -p /var/lib/mesos/cni/conf.d

# Add location of binary and conf directories for CNI.
echo '/var/lib/mesos/cni/plugins' | tee /etc/mesos-slave/network_cni_plugins_dir
echo '/var/lib/mesos/cni/conf.d' | tee /etc/mesos-slave/network_cni_config_dir


# find /etc/mesos-slave/* | xargs cat


#
cd /var/lib/mesos/cni/plugins
wget https://github.com/containernetworking/cni/releases/download/v0.3.0/cni-v0.3.0.tgz
tar xvf cni-*.tgz


## Install go:
# curl -O https://storage.googleapis.com/golang/go1.6.linux-amd64.tar.gz
# tar -xvf go1.6.linux-amd64.tar.gz
# mv go /usr/local
# export PATH=$PATH:/usr/local/go/bin
# export GOPATH=$HOME

## Install CNI plugins:
# git clone https://github.com/containernetworking/cni.git
# cd cni
# git checkout v0.3.0
# ./build
# cp bin/* /var/lib/mesos/cni/plugins



# https://github.com/containernetworking/cni
# https://github.com/containernetworking/cni/blob/master/SPEC.md
#--------------

# Add example Mesos CNI plugin configuration
cat << '__EOF__' | tee /var/lib/mesos/cni/conf.d/10-bridge.conf
{
    "cniVersion": "0.3.0",
    "name": "bridge-10-200",
    "type": "bridge",
    "bridge": "cni0",
    "isGateway": true,
    "ipMasq": true,
    "ipam": {
        "type": "host-local",
        "subnet": "10.200.0.0/16",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ]
    }
}
__EOF__


#
cat << '__EOF__' | tee /var/lib/mesos/cni/conf.d/99-loopback.conf
{
    "cniVersion": "0.3.0",
    "type": "loopback"
}
__EOF__



# systemctl restart mesos-slave
# systemctl status mesos-slave







# CoreOS Etcd – A highly available key-value store for shared configuration and service discovery.
# CoreOS Etcd is used by Calico to store network configurations.


# create directory /var/lib/etcd, /etc/etcd, add the etcd user and group:

mkdir /var/lib/etcd
mkdir /etc/etcd 

groupadd -r etcd
useradd -r -g etcd -d /var/lib/etcd -s /sbin/nologin -c "etcd user" etcd

chown -R etcd:etcd /var/lib/etcd


#
https://github.com/coreos/etcd/releases/download/v3.0.15/etcd-v3.0.15-linux-amd64.tar.gz
tar xvf etcd-*.tar.gz

cp etcd /usr/local/bin/
cp etcdctl /usr/local/bin/








# https://docs.onegini.com/cim/idp/2.39.01-SNAPSHOT/installation/etcd.html
# https://n40lab.wordpress.com/2016/08/01/installing-coreos-etcd-server-on-centos-7/
# http://severalnines.com/blog/mysql-docker-multi-host-networking-mysql-containers-part-2-calico





















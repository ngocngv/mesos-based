


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





## Installation

# Download the Calico CNI plugin to the $NETWORK_CNI_PLUGINS_DIR you configured for Mesos:
export NETWORK_CNI_PLUGINS_DIR=/var/lib/mesos/cni/plugins

curl -L -o $NETWORK_CNI_PLUGINS_DIR/calico https://github.com/projectcalico/calico-cni/releases/download/v1.5.1/calico

chmod +x $NETWORK_CNI_PLUGINS_DIR/calico
ln -s $NETWORK_CNI_PLUGINS_DIR/calico $NETWORK_CNI_PLUGINS_DIR/calico-ipam



# Run calico/node, a Docker container with calico’s core routing processes. 
# The calico/node container can easily be launched using calicoctl, Calico’s command line tool. 
# When doing so, we must provide the location of the running etcd instance by setting the ECTD_AUTHORITY environment variable.

curl -L -o /usr/local/bin/calicoctl https://github.com/projectcalico/calico-containers/releases/download/v0.23.0/calicoctl

chmod +x /usr/local/bin/calicoctl

ETCD_ENDPOINTS=http://<etcd-ip:port> ./calicoctl node


































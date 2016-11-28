


# Installing Calico-CNI for the Unified Containerizer
# http://docs.projectcalico.org/v2.0/getting-started/mesos/installation/unified



# How to add Calico networking to a Mesos Agent with CNI enabled.


# Prerequisites

# When enabling CNI in Mesos, you will have specified a network_cni_config_dir and network_cni_plugins_dir. 
# We’ll refer to these going forward as $NETWORK_CNI_CONFIG_DIR and $NETWORK_CNI_PLUGINS_DIR, respectively.


# Make dirs if they don't exist
mkdir -p /data/mesos/cni/plugins
mkdir -p /data/mesos/cni/conf.d

# Add location of binary and conf directories for CNI.
echo '/data/mesos/cni/plugins' | tee /etc/mesos-slave/network_cni_plugins_dir
echo '/data/mesos/cni/conf.d' | tee /etc/mesos-slave/network_cni_config_dir


#
cd /data/mesos/cni/plugins
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
# cp bin/* /data/mesos/cni/plugins





# Add example Mesos CNI plugin configuration

echo '{
"name": "cni-test",
"type": "bridge",
"bridge": "mesos-cni0",
"isGateway": true,
"ipMasq": true,
"ipam": {
    "type": "host-local",
    "subnet": "192.168.0.0/16",
    "routes": [
    { "dst":
      "0.0.0.0/0" }
    ]
  }
}' | sudo tee /etc/cni/net.d/bridge.conf


# mkdir -p /etc/cni/net.d
# cat >/etc/cni/net.d/10-mynet.conf <<EOF
{
    "cniVersion": "0.2.0",
    "name": "mynet",
    "type": "bridge",
    "bridge": "cni0",
    "isGateway": true,
    "ipMasq": true,
    "ipam": {
        "type": "host-local",
        "subnet": "10.22.0.0/16",
        "routes": [
            { "dst": "0.0.0.0/0" }
        ]
    }
}
EOF

# cat >/etc/cni/net.d/99-loopback.conf <<EOF
{
    "cniVersion": "0.2.0",
    "type": "loopback"
}
EOF






























# Installing Calico-CNI for the Unified Containerizer
# http://docs.projectcalico.org/v2.0/getting-started/mesos/installation/unified



# How to add Calico networking to a Mesos Agent with CNI enabled.


# Prerequisites

# When enabling CNI in Mesos, you will have specified a network_cni_config_dir and network_cni_plugins_dir. 
# We’ll refer to these going forward as $NETWORK_CNI_CONFIG_DIR and $NETWORK_CNI_PLUGINS_DIR, respectively.

echo '/data/mesos/cni/config' | tee /etc/mesos-slave/network_cni_config_dir
#
echo '/data/mesos/cni/plugins' | tee /etc/mesos-slave/network_cni_plugins_dir

#
mkdir -p /data/mesos/cni/config
mkdir -p /data/mesos/cni/plugins


echo '/var/lib/mesos/cni/config' | tee /etc/mesos-slave/network_cni_config_dir
echo '/var/lib/mesos/cni/plugins' | tee /etc/mesos-slave/network_cni_plugins_dir

--network_cni_config_dir=/var/lib/mesos/cni/config
--network_cni_plugins_dir=/var/lib/mesos/cni/plugins








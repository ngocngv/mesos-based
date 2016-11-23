


# Configuring the slave pool


# Installing the repository
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm


# Installing Mesos
yum -y install mesos


# Configuring Mesos
#--------------------------------------------------------------------------

# The same as the master nodes, you need to edit your /etc/mesos/zk informing the ZK url of your master cluster:
echo zk://master-1:2181,master-2:2181,master-3:2181,master-4:2181,master-5:2181/mesos > /etc/mesos/zk


# Disabling Mesos master in the slave nodes
systemctl stop mesos-master  
systemctl disable mesos-master


# Restarting Mesos
systemctl restart mesos-slave  
















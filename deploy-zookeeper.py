#!/usr/bin/python


# Install JRE
# yum install java-1.8.0-openjdk

# Install JDK
# yum install java-1.8.0-openjdk-devel

# openjdk version "1.8.0_111"
# OpenJDK Runtime Environment (build 1.8.0_111-b15)
# OpenJDK 64-Bit Server VM (build 25.111-b15, mixed mode)



# Installing the repository
# rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-3.noarch.rpm


# Installing Zookeeper in the master pool
yum -y install mesosphere-zookeeper


# Configuring Zookeeper
# Set /etc/zookeeper/conf/myid to the id of the current master.
echo '1' > /etc/zookeeper/conf/myid


# Configure /etc/zookeeper/conf/zoo.cfg, informing each machine our cluster will have.
cp /etc/zookeeper/conf/zoo.cfg /etc/zookeeper/conf/zoo.cfg.bak
#
cat << EOF | tee /etc/zookeeper/conf/zoo.cfg
# the maximum number of client connections.
# increase this if you need to handle more clients
maxClientCnxns=60
# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial 
# synchronization phase can take
initLimit=10
# The number of ticks that can pass between 
# sending a request and getting an acknowledgement
syncLimit=5
# the directory where the snapshot is stored.
dataDir=/var/lib/zookeeper
# the port at which the clients will connect
clientPort=2181
#
server.1=master-1:2888:3888
EOF















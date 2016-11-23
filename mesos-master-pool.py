

# http://www.thedevpiece.com/building-a-microservice-infrastructure-using-mesos-marathon-and-zookeeper/


# Building a Microservice Infrastructure using Mesos, Marathon and Zookeeper


# master pool, slave pool, proxy pool


# Installing the repository
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm


# Installing Zookeeper, Marathon and Mesos in the master pool
yum -y install mesos marathon mesosphere-zookeeper


# Configuring Zookeeper
#--------------------------------------------------------------------------
# Set /etc/zookeeper/conf/myid to the id of the current master.
echo 1 > /etc/zookeeper/conf/myid

# Configure /etc/zookeeper/conf/zoo.cfg, informing each machine our cluster will have.
server.1=master-1:2888:3888  
server.2=master-2:2888:3888  
server.3=master-3:2888:3888  
server.4=master-4:2888:3888  
server.5=master-5:2888:3888


# Configuring Mesos
#--------------------------------------------------------------------------
# Now, you need to edit your /etc/mesos/zk informing the ZK url of your cluster:
echo zk://master-1:2181,master-2:2181,master-3:2181,master-4:2181,master-5:2181/mesos >  /etc/mesos/zk

# Since we have five master machines, the mesos quorum will be three:
echo 3 > /etc/mesos-master/quorum



# Disabling Mesos slave on the master nodes
systemctl stop mesos-slave  
systemctl disable mesos-slave


# Configuring Marathon
#--------------------------------------------------------------------------
# Add the following lines to /etc/sysconfig/marathon:
MARATHON_EVENT_SUBSCRIBER=http_callback  
MARATHON_TASK_LAUNCH_TIMEOUT=600000  
MARATHON_TASK_LOST_EXPUNGE_GC=60000  
MARATHON_TASK_LOST_EXPUNGE_INITIAL_DELAY=60000  
MARATHON_TASK_LOST_EXPUNGE_INTERVAL=60000  


# Restarting Mesos, Marathon and Zookeeper
systemctl restart zookeeper  
systemctl restart mesos-master  
systemctl restart marathon






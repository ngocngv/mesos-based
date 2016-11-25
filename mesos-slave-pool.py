


# Configuring the slave pool


# Installing the repository
# rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-3.noarch.rpm

# Installing Mesos
yum -y install mesos


# Configuring Mesos
#--------------------------------------------------------------------------
# Extra config for Mesos:

# The same as the master nodes, you need to edit your /etc/mesos/zk informing the ZK url of your master cluster:
# echo zk://master-1:2181,master-2:2181,master-3:2181,master-4:2181,master-5:2181/mesos > /etc/mesos/zk
echo "zk://master-1:2181,master-2:2181,master-3:2181,master-4:2181,master-5:2181/mesos" | tee /etc/mesos/zk
          
# To ensure that mesos-slave is listening on a specific interface:
# echo "ipaddr" | tee /etc/mesos-slave/ip

# Mesos slave hostname:
# echo "mesos-slave.ipaddr" | tee /etc/mesos-slave/hostname

            

# Disabling Mesos master in the slave nodes
systemctl stop mesos-master  
systemctl disable mesos-master


# Restarting Mesos
systemctl restart mesos-slave  




# Test network connection with Mesos Master node
#------------------------------------------------------------------------------------------
# Ping the mesos-master at its ip address
# ping -c "ipaddr"

# Test if the port 2181, used by ZooKeeper on the Mesos Master node, is open
# telnet "master-1" 2181 


# Test mesos-slave service
ps aux | grep mesos-slave
systemctl status mesos-slave


## Test the Mesos Slave node:
# A slave node is registered into the Mesos Master

## Test the Cluster:
# Connection Mesos Slave -> Mesos Master
mesos-resolve `cat /etc/mesos/zk`


## Launch task from Mesos Slave node:
# Best way to test: launch a task through mesos-execute from mesos-slave node

# Set the MASTER
export MASTER=$(mesos-resolve `cat /etc/mesos/zk`)
echo $MASTER

# Launch the task
mesos-execute --master=$MASTER --name="cluster-test" --command="sleep 5"


















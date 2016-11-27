

# Installing the repository
# rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-3.noarch.rpm


  
# Installing Zookeeper, Marathon and Mesos in the master pool
# yum -y install mesos
yum -y install mesos-1.1.0




# Configuring Mesos
# edit /etc/mesos/zk informing the ZK url of your cluster:
echo "zk://master-1:2181,master-2:2181,master-3:2181,master-4:2181,master-5:2181/mesos" | tee /etc/mesos/zk
   



# systemctl enable mesos-master
# systemctl enable mesos-slave

# systemctl start mesos-master
# systemctl start mesos-slave





















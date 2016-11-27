

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




# Firewall Changes
# Open Ports 5050,5051,2181,2888,3888

firewall-cmd --permanent --zone=public --add-port=5050/tcp    # mesos-master
firewall-cmd --permanent --zone=public --add-port=5051/tcp    # mesos-slave
firewall-cmd --permanent --zone=public --add-port=8080/tcp    # marathon
firewall-cmd --permanent --zone=public --add-port=4400/tcp    # chronos
firewall-cmd --reload


-A INPUT -p tcp -m state --state NEW -m tcp --dport 2181 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 5050 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 5051 -j ACCEPT
-A INPUT -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT


















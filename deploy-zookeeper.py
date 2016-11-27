#!/usr/bin/python

# http://davidssysadminnotes.blogspot.com/2016/06/setting-up-apache-mesos-cluster-centos-7.html


## Install JRE
# yum install java-1.8.0-openjdk

## Install JDK
# yum install java-1.8.0-openjdk-devel

## Install Zookeeper
# - Unzipped 3.4.8 to opt folder
# - Created user zookeeper (useradd zookeeper)
# - Created symbolic link (ln -s zookeeper zookeeper-3.4.8)
# - Set owner/group of all file to zookeeper 



# Installing the repository
# rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-3.noarch.rpm


# Installing Zookeeper in the master pool
yum -y install mesosphere-zookeeper



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



# - Created /var/lib/zookeeper; also set owner to zookeeper:zookeeper
# - Created myid file contents of "1"
# - Created zookeeper.service in /etc/systemd/system folder

# Configuring Zookeeper
# Set /etc/zookeeper/conf/myid to the id of the current master.
echo '1' > /etc/zookeeper/conf/myid


# /usr/lib/systemd/system/zookeeper.service
#--------------------------------------------------------------------------------
[Unit]
Description=Apache ZooKeeper
After=network.target
ConditionPathExists=/etc/zookeeper/conf/zoo.cfg
ConditionPathExists=/etc/zookeeper/conf/log4j.properties

[Service]
Environment="ZOOCFGDIR=/etc/zookeeper/conf"
SyslogIdentifier=zookeeper
WorkingDirectory=/opt/mesosphere/zookeeper
ExecStart=/opt/mesosphere/zookeeper/bin/zkServer.sh start-foreground
Restart=on-failure
RestartSec=20
User=root
Group=root

[Install]
WantedBy=multi-user.target



# /etc/systemd/system/zookeeper.service
#--------------------------------------------------------------------------------
[Unit]
Description=Apache Zookeeper server
Documentation=http://zookeeper.apache.org
Requires=network.target remote-fs.target
After=network.target remote-fs.target

[Service]
Type=forking
User=zookeeper
Group=zookeeper
ExecStart=/opt/zookeeper/bin/zkServer.sh start
ExecStop=/opt/zookeeper/bin/zkServer.sh stop
ExecReload=/opt/zookeeper/bin/zkServer.sh restart
WorkingDirectory=/var/lib/zookeeper

[Install]
WantedBy=multi-user.target




## Loaded
systemctl daemon-reload
systemctl enable zookeeper
systemctl start zookeeper








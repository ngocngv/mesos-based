

# Installing the repository
# rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-1.noarch.rpm
rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-repo-7-3.noarch.rpm




# Installing Marathon in the master pool
yum -y install marathon






# Configuring Marathon
#--------------------------------------------------------------------------
# Add the following lines to /etc/sysconfig/marathon:
# MARATHON_EVENT_SUBSCRIBER=http_callback  
# MARATHON_TASK_LAUNCH_TIMEOUT=600000  
# MARATHON_TASK_LOST_EXPUNGE_GC=60000  
# MARATHON_TASK_LOST_EXPUNGE_INITIAL_DELAY=60000  
# MARATHON_TASK_LOST_EXPUNGE_INTERVAL=60000  

cat << EOF | tee /etc/sysconfig/marathon
MARATHON_EVENT_SUBSCRIBER=http_callback
MARATHON_TASK_LAUNCH_TIMEOUT=600000
MARATHON_TASK_LOST_EXPUNGE_GC=60000
MARATHON_TASK_LOST_EXPUNGE_INITIAL_DELAY=60000
MARATHON_TASK_LOST_EXPUNGE_INTERVAL=60000
EOF







# Restarting Marathon
systemctl enable marathon
systemctl start marathon
systemctl restart marathon


















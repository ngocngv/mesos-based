



# configure slave machines to also be able to run docker containers:
echo 'docker,mesos' > /etc/mesos-slave/containerizers

# Increase the executor timeout to account for the potential delay pulling a docker image to the agent node.
# echo '5mins' > /etc/mesos-slave/executor_registration_timeout
echo '10mins' > /etc/mesos-slave/executor_registration_timeout

# Restart the agent process to load the new configuration.






# systemctl enable mesos-slave
# systemctl start mesos-slave



















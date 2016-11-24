

# Configuring your Mesos slaves to run Docker containers


# install docker in all slave machines:

yum check-update  
curl -fsSL https://get.docker.com/ | sh


#
systemctl enable docker
systemctl start docker


# configure slave machines to also be able to run docker containers:
echo 'docker,mesos' > /etc/mesos-slave/containerizers

# And increase the executor timeout for a possible delay in downloading an image:
echo '5mins' > /etc/mesos-slave/executor_registration_timeout































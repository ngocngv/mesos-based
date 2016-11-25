
# http://www.thedevpiece.com/deploying-and-running-docker-containers-on-marathon/
# https://mesosphere.github.io/marathon/docs/native-docker.html



# Configuring Mesos slaves to run Docker containers


# install docker in all slave machines:

yum check-update  
curl -fsSL https://get.docker.com/ | sh


#
systemctl enable docker
systemctl start docker


# configure slave machines to also be able to run docker containers:
echo 'docker,mesos' > /etc/mesos-slave/containerizers

# Increase the executor timeout to account for the potential delay pulling a docker image to the agent node.
# echo '5mins' > /etc/mesos-slave/executor_registration_timeout
echo '10mins' > /etc/mesos-slave/executor_registration_timeout

# Restart the agent process to load the new configuration.




# Configuring Mesos slaves to use a private docker registry
#--------------------------------------------------------------------------

# If you want to set up Marathon to run your Docker images, you need to do the following steps:
docker login docker.registry.com

# After login in, you need to tar your credentials:
cd ~ && tar czf docker.tar.gz .docker




# Deploying your application into Marathon


















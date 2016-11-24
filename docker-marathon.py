
# http://www.thedevpiece.com/deploying-and-running-docker-containers-on-marathon/

# Configuring Mesos slaves to run Docker containers


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



# Configuring Mesos slaves to use a private docker registry
#--------------------------------------------------------------------------

# If you want to set up Marathon to run your Docker images, you need to do the following steps:
docker login docker.registry.com

# After login in, you need to tar your credentials:
cd ~ && tar czf docker.tar.gz .docker




# Deploying your application into Marathon


















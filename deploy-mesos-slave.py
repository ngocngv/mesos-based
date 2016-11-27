

# http://mesos.apache.org/documentation/latest/container-image/



# configure slave machines to also be able to run docker containers:
echo 'docker,mesos' | tee /etc/mesos-slave/containerizers

# Increase the executor timeout to account for the potential delay pulling a docker image to the agent node.
# echo '5mins' > /etc/mesos-slave/executor_registration_timeout
echo '10mins' | tee /etc/mesos-slave/executor_registration_timeout

#
# echo '/var/lib/mesos' > /etc/mesos-slave/work_dir
echo '/data/mesos' | tee /etc/mesos-slave/work_dir

# allows both Docker and Appc container images
# echo 'docker,appc' | tee /etc/mesos-slave/image_providers

# allow containers to use Docker 
echo 'docker' | tee /etc/mesos-slave/image_providers

# The operator needs to add the following isolators
echo 'filesystem/linux,docker/runtime' | tee /etc/mesos-slave/isolation

# - filesystem/linux: 
# This is needed because supporting container images involves changing filesystem root, and only filesystem/linux support that currently. 
# Note that this isolator requires root permission.

# - docker/runtime: 
# This is used to provide support for runtime configurations specified in Docker images (e.g., Entrypoint/Cmd, environment variables, etc.). 
# See more details about this isolator in Mesos containerizer doc. http://mesos.apache.org/documentation/latest/mesos-containerizer/
# Note that if this isolator is not specified and --image_providers contains docker, the agent will refuse to start.


  
  

# Restart the agent process to load the new configuration.






# systemctl enable mesos-slave
# systemctl start mesos-slave





















# Calico-Mesos Usage Guide with the Docker Containerizer
# http://docs.projectcalico.org/v2.0/getting-started/mesos/tutorials/docker



# Creating a Docker network and managing network policy
docker network create --driver calico --ipam-driver calico-ipam management-database
docker network create --driver calico --ipam-driver calico-ipam management-ui

docker network create --driver=calico --ipam-driver=calico-ipam my-calico-net






curl -X POST -H "Content-Type:application/json" http://118.69.190.27:8080/v2/apps?force=true --data '
{
  "id": "dockercloud-hello-world",
  "container": {
    "type": "DOCKER",
    "docker": {
      "image": "dockercloud/hello-world",
      "network": "BRIDGE",
      "portMappings": [
        { "hostPort": 0, "containerPort": 80 }
      ],
      "forcePullImage":true
    }
  },
  "instances": 2,
  "cpus": 0.1,
  "mem": 128,
  "healthChecks": [{
      "protocol": "HTTP",
      "path": "/",
      "portIndex": 0,
      "timeoutSeconds": 10,
      "gracePeriodSeconds": 10,
      "intervalSeconds": 2,
      "maxConsecutiveFailures": 10
  }],
  "labels":{
    "HAPROXY_GROUP":"external",
    "HAPROXY_0_VHOST":"dockercloud-hello-world.${FQN}"
  }
}'


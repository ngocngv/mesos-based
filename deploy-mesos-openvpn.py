

# http://blog.bdgn.net/a-reference-mesos-cluster-setup-3




# Marathon config for OpenVPN
#-----------------------------------------------------------------------

cat << '__EOF__' | tee openvpn-marathon.json
{
  "id": "/openvpn",
  "container": {
    "type": "DOCKER",
    "docker": {
      "image": "docker-registry.marathon.mesos:5000/openvpn",
      "network": "USER",
      "portMappings": [
        { "hostPort": 0, 
          "containerPort": 8080
        }
      ],
      "forcePullImage":true
    }
  },  
  "instances": 1,
  "cpus": 0.1,
  "mem": 128,
  "ipAddress": {
      "networkName": "management-ui"
  },

  "dependencies": ["/mesos-dns", "/docker-registry"],
  "healthChecks": [{"protocol": "TCP"}]
}
__EOF__



# Starting the OpenVPN service:
curl -sL -X POST \
  -H 'content-type: application/json' \
  leader.mesos:8080/v2/apps \
  -d@openvpn-marathon.json | jq .


























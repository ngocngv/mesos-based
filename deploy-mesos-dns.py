


# http://blog.bdgn.net/a-reference-mesos-cluster-setup-2


cat << '__EOF__' | tee mesos-dns-marathon.json
{
  "cpus": 0.1,
  "mem": 32,
  "id": "/mesos-dns",
  "instances": 3,
  "constraints": [
    ["master", "CLUSTER", "true"],
    ["hostname", "UNIQUE"]
  ],
  "env": {
    "MESOS_DNS_ZK": "zk://$MASTER_1:2181,$MASTER_2:2181,$MASTER_3:2181/mesos",
    "MESOS_DNS_RESOLVERS": "8.8.8.8",
    "MESOS_DNS_REFRESHSECONDS": "10",
    "MESOS_DNS_TTL": "10",
  },
  "container": {
    "docker": { "image": "bergerx/mesos-dns" }
  },
  "healthChecks": [{
    "protocol": "COMMAND",
    "command": { "value": "dig A leader.mesos @$HOST | grep 'status: NOERROR'" }
  }],
  "upgradeStrategy": {
    "minimumHealthCapacity": 0.5,
    "maximumOverCapacity": 0
  }
}
__EOF__



cat << '__EOF__' | tee mesos-dns-marathon.json
{
  "id": "/mesos-dns",
  "container": {
    "type": "DOCKER",
    "docker": {
      "image": "bergerx/mesos-dns",
      "network": "USER",
      "portMappings": [
        { "hostPort": 0, "containerPort": 8080 }
      ],
      "forcePullImage":true
    }
  },
  "instances": 1,
  "cpus": 0.1,
  "mem": 32,
  "ipAddress": {
      "networkName": "management-ui"
  },  
  "env": {
    "MESOS_DNS_ZK": "zk://$MASTER_1:2181,$MASTER_2:2181,$MASTER_3:2181/mesos",
    "MESOS_DNS_RESOLVERS": "8.8.8.8",
    "MESOS_DNS_REFRESHSECONDS": "10",
    "MESOS_DNS_TTL": "10",
  },
  "healthChecks": [{
    "protocol": "COMMAND",
    "command": { "value": "dig A leader.mesos @$HOST | grep 'status: NOERROR'" }
  }],
  "upgradeStrategy": {
    "minimumHealthCapacity": 0.5,
    "maximumOverCapacity": 0
  }
}
__EOF__




curl \
  -X POST \
  -H 'Content-Type: application/json' \
  -d@mesos-dns-marathon.json \
  $MASTER_1:8080/v2/apps | jq .











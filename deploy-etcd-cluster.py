

# CoreOS Etcd – A highly available key-value store for shared configuration and service discovery.
# CoreOS Etcd is used by Calico to store network configurations.


# create directory /var/lib/etcd, /etc/etcd, add the etcd user and group:

mkdir /var/lib/etcd
mkdir /etc/etcd 

groupadd -r etcd
useradd -r -g etcd -d /var/lib/etcd -s /sbin/nologin -c "etcd user" etcd

chown -R etcd:etcd /var/lib/etcd


#
https://github.com/coreos/etcd/releases/download/v3.0.15/etcd-v3.0.15-linux-amd64.tar.gz
tar xvf etcd-*.tar.gz

cp etcd /usr/local/bin/
cp etcdctl /usr/local/bin/






# https://docs.onegini.com/cim/idp/2.39.01-SNAPSHOT/installation/etcd.html
# https://n40lab.wordpress.com/2016/08/01/installing-coreos-etcd-server-on-centos-7/
# http://severalnines.com/blog/mysql-docker-multi-host-networking-mysql-containers-part-2-calico


#
# edit /etc/etcd/etcd.conf
#----------------------------------------------------------------------------------
cat << '__EOF__' | tee /etc/etcd/etcd.conf
# [member]
ETCD_NAME="etcd_1"
ETCD_DATA_DIR="/var/lib/etcd/default.etcd"
#ETCD_WAL_DIR=""
#ETCD_SNAPSHOT_COUNT="10000"
#ETCD_HEARTBEAT_INTERVAL="100"
#ETCD_ELECTION_TIMEOUT="1000"
#ETCD_LISTEN_PEER_URLS="http://127.0.0.1:2380"
ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380"
#ETCD_LISTEN_CLIENT_URLS="http://127.0.0.1:2379"
#ETCD_LISTEN_CLIENT_URLS="http://127.0.0.1:2379,http://172.17.42.1:2379,http://172.16.181.132:2379"
ETCD_LISTEN_CLIENT_URLS="http://0.0.0.0:2379"
#ETCD_MAX_SNAPSHOTS="5"
#ETCD_MAX_WALS="5"
#ETCD_CORS=""

# [cluster]
ETCD_INITIAL_ADVERTISE_PEER_URLS="http://127.0.0.1:2380"
ETCD_INITIAL_CLUSTER="etcd_1=http://127.0.0.1:2380"
ETCD_INITIAL_CLUSTER_STATE="new"
ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-1"
#
#ETCD_ADVERTISE_CLIENT_URLS="http://127.0.0.1:2379"
#ETCD_ADVERTISE_CLIENT_URLS="http://127.0.0.1:2379,http://172.17.42.1:2379,http://172.16.181.132:2379"
ETCD_ADVERTISE_CLIENT_URLS="http://0.0.0.0:2379"
#ETCD_DISCOVERY=""
#ETCD_DISCOVERY_SRV=""
#ETCD_DISCOVERY_FALLBACK="proxy"
#ETCD_DISCOVERY_PROXY=""
#ETCD_STRICT_RECONFIG_CHECK="false"

#[proxy]
#ETCD_PROXY="off"
#ETCD_PROXY_FAILURE_WAIT="5000"
#ETCD_PROXY_REFRESH_INTERVAL="30000"
#ETCD_PROXY_DIAL_TIMEOUT="1000"
#ETCD_PROXY_WRITE_TIMEOUT="5000"
#ETCD_PROXY_READ_TIMEOUT="0"

#[security]
#ETCD_CERT_FILE=""
#ETCD_KEY_FILE=""
#ETCD_CLIENT_CERT_AUTH="false"
#ETCD_TRUSTED_CA_FILE=""
#ETCD_PEER_CERT_FILE=""
#ETCD_PEER_KEY_FILE=""
#ETCD_PEER_CLIENT_CERT_AUTH="false"
#ETCD_PEER_TRUSTED_CA_FILE=""

#[logging]
#ETCD_DEBUG="false"
# examples for -log-package-levels etcdserver=WARNING,security=DEBUG
#ETCD_LOG_PACKAGE_LEVELS=""

#[profiling]
#ETCD_ENABLE_PPROF="false"
__EOF__







# edit /usr/lib/systemd/system/etcd.service
#------------------------------------------------------------------------------------
cat << '__EOF__' | tee /etc/systemd/system/etcd.service
[Unit]
Description=Etcd Cluster
After=network.target
After=network-online.target
Wants=network-online.target

[Service]
Type=notify
WorkingDirectory=/var/lib/etcd/
EnvironmentFile=-/etc/etcd/etcd.conf
User=etcd
# set GOMAXPROCS to number of processors
# ExecStart=/bin/bash -c "GOMAXPROCS=$(nproc) /usr/bin/etcd --name=\"${ETCD_NAME}\" --data-dir=\"${ETCD_DATA_DIR}\" --listen-client-urls=\"${ETCD_LISTEN_CLIENT_URLS}\""
ExecStart=/usr/local/bin/etcd
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

__EOF__






# systemctl enable etcd
# systemctl start etcd

# systemctl status etcd


















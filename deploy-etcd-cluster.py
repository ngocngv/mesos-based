

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


















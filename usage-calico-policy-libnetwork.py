

# Accessing Calico policy with Calico as a network plugin
# http://docs.projectcalico.org/v2.0/getting-started/docker/tutorials/advanced-policy




docker network create --driver calico --ipam-driver calico-ipam database 
docker network create --driver calico --ipam-driver calico-ipam frontend 



# Create the profiles
# Profile Resource (profile)
# http://docs.projectcalico.org/v2.0/reference/calicoctl/resources/profile

# Use calicoctl apply to create or update the profiles:
#------------------------------------------------------------------------------
cat << '__EOF__' | /usr/local/bin/calicoctl apply -f -
- apiVersion: v1
  kind: profile
  metadata:
    name: database
    labels:
      role: database
  spec:
    ingress:
    - action: allow
      protocol: tcp
      source:
        selector: role == 'frontend'
      destination:
        ports:
        -  3306
    - action: allow
      source:
        selector: role == 'database'
    egress:
    - action: allow
      destination:
        selector: role == 'database'
- apiVersion: v1
  kind: profile
  metadata:
    name: frontend
    labels:
      role: frontend
  spec:
    egress:
    - action: allow
      protocol: tcp
      destination:
        selector: role == 'database'
        ports:
        -  3306
__EOF__














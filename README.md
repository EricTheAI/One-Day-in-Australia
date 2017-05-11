# One Day in Melbourne
## Installing Ansible

```
$ sudo apt-get update
$ sudo apt-get install ansible
```

## Playbooks

There are 2 playbooks for creating a new instance on NeCTAR and installing all required packages and dependencies for tweet harvester and analysing.

- `launch-create-attach.yaml` using module nova_compute to create a new instance on openstack(the parameters nodename and flavorid need to be provided).
- `vmount-app.yaml` for volume to be attached to the instance, format it to ext4 and mount it under `/mnt/data`, then create directory couchdb.

Use the  `install.sh` script to run these plays.

## Steps:

1. Store the private key at local machine.
2. Run  `bash install.sh`, there will be 2 options for choosing.
3. Enter `1` to launch a new instance, create a volume and attach it, then enter node name, flavor id and volume name.
4. Or enter `2` to mount volume and install required software packages and dependencies, CouchDB and then automatically configure it.
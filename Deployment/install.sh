# sh file

echo "1. Launch a new instance and create a volume.	2. Mount /mnt/data file and install basic tools."
read OPT
echo ""

if [ "$OPT" -eq 1 ]; then
	echo "Please enter node name:"
	read NODENAME
	echo "Please enter flavor id:"
	read FLAVORID
	echo "Please enter volume name:"
	read VOLUMENAME
	sudo ansible-playbook launch-create-attach.yaml --extra-vars "nodename=$NODENAME flavorid=$FLAVORID volumename=$VOLUMENAME"

	else
		if [ "$OPT" -eq 2 ]; then
			echo "Please enter hostname:"
			read HOSTS
			sudo ansible-playbook vmount-app.yaml -u ubuntu --private-key=~/ansible_playbook/ansible_test.key #--extra-vars "hosts=$HOSTS"
		fi
fi
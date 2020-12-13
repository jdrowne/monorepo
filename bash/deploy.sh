#!/bin/bash
POSITIONAL=()
while [[ $# -gt 0 ]]; do
  key="$1"
  case $key in
    --subnet_id)
    subnet_id="$2"
    shift # past argument
    shift # past value
    ;;
    *)    # unknown option
    POSITIONAL+=("$1") # save it in an array for later
    shift # past argument
    ;;
  esac
done
set -- "${POSITIONAL[@]}" # restore positional parameters
echo "Installing Ansible"
sudo yum install -y ansible
if [ -z "$subnet_id" ]
then
  ansible-playbook -v ansible/site.yml
else
  ansible-playbook -v ansible/site.yml --extra-vars "subnet_id=${subnet_id}"
fi

# ansible-python-script
A simple ansible python script demo 
# Install Dependencies 
## Get pip
sudo apt-get install -y python-pip

## Get virtualenv and create one
sudo pip install virtualenv
cd /path/to/runner/script
virtualenv ./.env
source ./env/bin/activate

## Install Ansible into the virtualenv
pip install ansible

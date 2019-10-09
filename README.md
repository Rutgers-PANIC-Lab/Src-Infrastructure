# Src-Infrastructure
Repo to hold stuff used for deploying infrastructure.

## Deployment Instructions
To deploy a new Panic or Parasol node, perform the following steps:
- Install Ubuntu 18.04 LTS (Server)
    - During installation, add a user as follows:   
    ```
    Name: Local Admin
    Username: localadmin
    Password: {{ lab standard }}
    ```  
    
    - When the new system comes online, execute the following to install Ansible
    (Select "Yes" to restart services without asking, if prompted.)
    ```
    sudo apt update && \
    sudo apt install --yes software-properties-common && \
    sudo apt-add-repository --yes --update ppa:ansible/ansible && \
    sudo apt install --yes ansible
    ```
    
    - Once ansible is installed, run the following commands (you can skip the ones that do not apply):
    ```
    sudo su
    cd
    # sets up kerberos and home directory
    ansible-pull -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure kerberos-init.yaml
    ansible-pull -f -U https://github.com/clhedrick/kerberos-ansible.git kerberos-boot.yml
    ansible-pull -f -U https://github.com/clhedrick/kerberos-ansible.git kerberos.yml
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git autofs.yaml

    # for machines with intel gpus (and a need for latest video encoding)
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git intel-gpu.yaml
    
    # for machines with nvidia gpus
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git cuda.yaml
    
    # for custom ffmpeg
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git ffmpeg.yaml
    
    # for docker
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git docker.yaml
    ```
    
    
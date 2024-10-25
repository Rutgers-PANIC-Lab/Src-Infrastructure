# Src-Infrastructure
Repo to hold stuff used for deploying infrastructure.

## Deployment Instructions

### **Current: Deploying a New Panic or Parasol Node with Ubuntu 22.04 LTS**

1. **Reboot target machine using IPMI**
    - Continually press F12 while it reboots so that it reboots from PXE/LAN

2. **Select Install Ubuntu 22 from Network**
    - Will restart over the course of roughly half an hour to 45 minutes
  
3. **Ensure home directory is present once it finishes**
    - If not, follow Step 2 in the old procedure below.
    
---


### **Old: Deploying a New Panic or Parasol Node with Ubuntu 22.04 LTS**

1. **Install Ubuntu 22.04 LTS (Server)**
    - During installation, create a user with the following credentials:   
    ```
    Name: Local Admin
    Username: localadmin
    Password: {{ lab standard }}
    ```  
    
2. **Kerberize Script Authorization**
    - To run the Kerberize script, you must either be staff/faculty or obtain authorization from Chunk (hedrick@rutgers.edu).
    - Execute the following commands to download and run the Kerberize script:
    ```
    sudo wget https://services.cs.rutgers.edu/kerberize
    sudo bash kerberize
    ```
    - For more information about the Kerberize process, please refer to [Kerberize Documentation](https://services.cs.rutgers.edu/kerberize.html).

3. **Setup Sudo**
    - **TODO:** Update the repository with the necessary files to add the sudo group.
    - This step involves setting up sudo access.

4. **Setup Home Directory**
    - **TODO:** Check and validate on Parasol machines later.
    - Run the following command to set up the home directory:
    ```
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git autofs.yaml
    ```
    - **Note:** This step is currently validated on the PANIC server but may have issues with Parasol machines.

5. **Fix LD_PRELOAD**
    - If you encounter the following error:
    ```
    ERROR: ld.so: object '/usr/lib/x86_64-linux-gnu/libGLEW.so' from LD_PRELOAD cannot be preloaded (cannot open shared object file): ignored.
    ```
    - Install the necessary library by running:
    ```
    sudo apt-get install libglew-dev
    ```
    
---

### **Archived: Deploying a New Panic or Parasol Node with Ubuntu 18.04 LTS**

1. **Install Ubuntu 18.04 LTS (Server)**
    - During installation, add a user as follows:   
    ```
    Name: Local Admin
    Username: localadmin
    Password: {{ lab standard }}
    ```  
    
2. **Install Ansible**
    - When the new system comes online, execute the following to install Ansible:
    (Select "Yes" to restart services without asking, if prompted.)
    ```
    sudo apt update && \
    sudo apt install --yes software-properties-common && \
    sudo apt-add-repository --yes --update ppa:ansible/ansible && \
    sudo apt install --yes ansible
    ```
    
3. **Run Ansible Playbooks**
    - Once Ansible is installed, run the following commands (skip the ones that do not apply):
    ```
    sudo su
    cd
    # Sets up Kerberos and home directory
    ansible-pull -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git kerberos-init.yaml
    ansible-pull -f -U https://github.com/clhedrick/kerberos-ansible.git kerberos-boot.yml
    ansible-pull -f -U https://github.com/clhedrick/kerberos-ansible.git kerberos.yml
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git autofs.yaml

    # For machines with Intel GPUs (and a need for latest video encoding)
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git intel-gpu.yaml
    
    # For machines with NVIDIA GPUs
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git cuda.yaml
    
    # For custom FFmpeg
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git ffmpeg.yaml
    
    # For Docker
    ansible-pull -f -U https://github.com/Rutgers-PANIC-Lab/Src-Infrastructure.git docker.yaml
    ```

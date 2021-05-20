#This is YMAL Configuration specifies a server with two volumes and two users

server:
    instance_type: t2.micro 
    ami_type: amzn2
    architecture: x86_64 #size and verision of vm system is trying to boot 
    root_device_type: ebs #where main file is being called from 
    virtualization_type: hvm
    min_count: 10 #seconds it takes to boot up vm 
    max_count: 10 #sceonds it takes to completely boot up vm 
    volumes:
        - device: /dev/xvda
          size_gb: 50 #This is the size the vm takes up when booting 
          type: ext 4
          mount: /
        - device: /dev/xvdf
          size_gb: 500 #This is the size the vm takes once it completes booting 
          type: xfs
          mount: /data
    users: #this allows users to enter into system using userscreen1 or userscreen2 
        - login: userscreen1
          ssh_key: --userscreen1 ssh public key goes here-- userscreen1@localhost
        - login: userscreen2
          ssh_key: --userscreen2 sshh public key goes here-- userscreen2@localhost
          
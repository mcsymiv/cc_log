## Setup
Note: examples is for MasOS
***
1. Check if ssh is on your system
###### Example:
```text
user@hostname:~$ shh
usage: ssh [-46sdfsfGsdfqsTtVvXxYy] [-B bind_interface]
           [-b bind_address] [-c cipher_spec] [-D [bind_address:]port]
           [-E log_file] [-e escape_char] [-F configfile] [-I pkcs11]
```
2. Generate .pem file from your .ppk private key
###### Example:
```text
user@hostname:~$ puttygen your-server.ppk -O private-openssh -o new-server.pem 
```
Note: -O is latin letter O (gr letter Omicron), not zero 0  
Check if putty installed on your machine. Otherwise:
```text
user@hostname:~$ brew install putty
```
3. Add your local machine to the server .known_hosts
```text
user@hostname:~$ ssh -i ~/path/private_key.pem remote-user@remote-host
```
If you see prompt with yes or no option - type "yes" and save.  
After, this retry previous command to create ssh session.
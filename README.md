# 888-DevOps-candidate-HS
This is the hiring assignment for Devops candidates at 888\Sparkware. It’s intended to mimic work you might do here, while giving us an understanding of your skills in: 

  - Windows System Administration
  - Scripting
  - Networking
  - Docker
  - Ansible
  - Git

## Preq
  - open git repo
 
## How to answer this assignment
To complete this assignment successfully, you'll need to perform all the tasks bellow and upload all requested artifacts to your git repo and share the git with us. 

## Windows

  - Build a Windows server (you can download predeployed windows 2016 ova from here: http://tinyurl.com/sol9vhc)
  - Write Ansible playbook to execute the following, and upload it to your git repo:
      * Install IIS and create a site which serves HTML page with "Hello World"
      * Create a self-signed certificate and bind it to the site you created in the previous bullet on port 443
      * Install dns service and create new zone(you can choose any domain name that you want)
  - Add a record to point the local web server you created, also make sure to create a record to perform dns reverse lookup
  - Add a small exe file or a an image to the web site you created and download it via HTTP(not via HTTPS). Record(sniff) the download session into a pcap file.
  - Filter the download session from the pcap file and create a screenshot, describe the communication steps steps in the session

## Scripting
  Use any scripting lanuguage (Prefered: Python or Powershell) to perform the following:
   - Read the the Dog API(https://dog.ceo/dog-api/) and write a script that can query the API and accepts the following parameters: --breed; --list; --count; --image
   
     --breed - [string] breed name (**mandatory**)
     
     --list - [boolean] if set returns the list of sub-breed
     
     --count - [boolean] if set returns count of sub-breed
     
     --image - [boolean] if set Download random image of the breed 
     
   - upload the script to your git repo 
     
## Docker

- Create a docker file to install linux server with nginx.
- Change the default port to 8080.
- Create an image out of it.
- Upload your docker script to your Git repo

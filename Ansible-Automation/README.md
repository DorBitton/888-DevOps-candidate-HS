## Windows

  - Build a Windows server (you can download predeployed windows 2016 ova from here: http://tinyurl.com/sol9vhc)
  
  I've created an EC2 instance from AWS so I can access from multiple devices.(with the right security group to allow outside connection)
  And a VMware Linux Ubuntu machine as the playbook runner. 
 
 We will add Ansible user
<img src="https://i.ibb.co/0nfw4Z8/computer-manag.jpg" alt="Terminal">
We will add the user to the Administrator group
<img src="https://i.ibb.co/hXG0WLQ/ansible-add.jpg" alt="Terminal">
<img src="https://i.ibb.co/r0F425P/Screenshot-from-2023-01-19-05-00-33.png" alt="Terminal">

  
  - Write Ansible playbook to execute the following, and upload it to your git repo:
      * Install IIS and create a site which serves HTML page with "Hello World"



```
- name: Install IIS and create site 
  hosts: all 
  tasks:
    - name: Install IIS
      win_feature:
        name: Web-Server
        state: present
        become: yes
    - name: Create Folder for site
      win_file:
        path: C:\inetpub\wwwroot\HelloWorld
        state: directory
    - name: Create IIS site
      win_iis_website:
        name: HelloWorld
        state: started
        physical_path: C:\inetpub\wwwroot\HelloWorld
        become: yes
        become_method: runas
    - name: Create HTML page for site
      win_file:
        path: C:\inetpub\wwwroot\HelloWorld\index.html
        state: touch
        become: yes
        become_method: runas
```
We can either Edit the content, or copy the .html files from Ubuntu to Windows server:
```
    - name: Add content to HTML page
      win_file:
        path: C:\inetpub\wwwroot\HelloWorld\index.html
        content: "Hello World"
        become: yes
        become_method: runas
```
```
    - name: Copy HTML page to Windows
      win_copy:
        src: /home/ansible/index.html
        dest: "C:\inetpub\wwwroot\HelloWorld\index.html"

```
* Create a self-signed certificate and bind it to the site you created in the previous bullet on port 443


      
      
      
* Install dns service and create new zone(you can choose any domain name that you want)
  - Add a record to point the local web server you created, also make sure to create a record to perform dns reverse lookup
  - Add a small exe file or a an image to the web site you created and download it via HTTP(not via HTTPS). Record(sniff) the download session into a pcap file.
  - Filter the download session from the pcap file and create a screenshot, describe the communication steps steps in the session

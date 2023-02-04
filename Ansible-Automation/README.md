## Windows

  - Build a Windows server (you can download predeployed windows 2016 ova from here: http://tinyurl.com/sol9vhc)
  
  I've created an EC2 instance from AWS so I can access from multiple devices.(with the right security group to allow outside connection)
  And a VMware Linux Ubuntu machine as the playbook runner. 
 
   Add Ansible user:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f306e6677345a382f636f6d70757465722d6d616e61672e6a7067.jpeg?raw=true" alt="Terminal">
 
   Add the user to the Administrator group:
 <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f68584730574c512f616e7369626c652d6164642e6a7067.jpeg?raw=true" alt="Terminal">

 Configure Windows Servers to Manage: Run the script in the PowerShell.
 
 ```
$url = "https://raw.githubusercontent.com/jborean93/ansible-windows/master/scripts/Upgrade-PowerShell.ps1"
$file = "$env:temp\Upgrade-PowerShell.ps1"
$username = "ansible"
$password = "ansible"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Force
&$file -Version 5.1 -Username $username -Password $password -Verbose
 ```
 To configure WinRM on a Windows system with ansible, a remote configuration script has been provided by ansible. Run the script in the PowerShell.
 
 ```
$url = "https://raw.githubusercontent.com/ansible/ansible/devel/examples/scripts/ConfigureRemotingForAnsible.ps1"
$file = "$env:temp\ConfigureRemotingForAnsible.ps1"
(New-Object -TypeName System.Net.WebClient).DownloadFile($url, $file)
powershell.exe -ExecutionPolicy ByPass -File $file
winrm enumerate winrm/config/Listener
 ```
 Set winrm to allow HTTP traffic & Set the authentication to basic in wirm.
```
winrm set winrm/config/service '@{AllowUnencrypted="true"}'
winrm set winrm/config/service/auth '@{Basic="true"}'

```

 Check the connection: 
 
<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f723046343235502f53637265656e73686f742d66726f6d2d323032332d30312d31392d30352d30302d33332e706e67.png?raw=true" alt="Terminal">

  
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
 Run Playbook:
 
<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f776750326344422f53637265656e73686f742d66726f6d2d323032332d30312d32322d32302d30322d31302e706e67.png?raw=true" alt="Terminal">



* Create a self-signed certificate and bind it to the site you created in the previous bullet on port 443

Create certificate:
```
openssl req -newkey rsa:4096 -x509 -sha256 -days 365 -nodes -out example.crt -keyout example.key
```
Add HTTPS binding to playbook:

```
   - name: Add a HTTPS binding
     community.windows.win_iis_webbinding:
       name: Default Web Site
       certificate_store_name: "/home/ansible/"
       protocol: https
       port: 443
       ip: 
       state: present
```
 Run:
 
<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f6859706762345a2f53637265656e73686f742d66726f6d2d323032332d30312d32322d32302d31302d30352e706e67.png?raw=true" alt="Terminal">

 
      
* Install dns service and create new zone(you can choose any domain name that you want)
 Add DNS install feature:
 
 ```
     - name: Install DNS
       win_feature:
         name: DNS
         state: present

 ```
 Run:
 
<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f72647364426d642f53637265656e73686f742d66726f6d2d323032332d30312d32322d32302d31392d35332e706e67.png?raw=true" alt="Terminal">


  - Add a record to point the local web server you created, also make sure to create a record to perform dns reverse lookup
  
  
  - Add a small exe file or a an image to the web site you created and download it via HTTP(not via HTTPS). Record(sniff) the download session into a pcap file.
  - Filter the download session from the pcap file and create a screenshot, describe the communication steps steps in the session

Enter website from mobile device:

<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/WhatsApp%20Image%202023-01-23%20at%2000.38.05.jpeg?raw=true" alt="Terminal" width="400" 
     height="500" > <img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/WhatsApp%20Image%202023-01-23%20at%2000.38.05(1).jpeg?raw=true" alt="Terminal" width="400" 
     height="500">

capture traffic with WireShark: filter by mobile device IP:

<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Ansible-Automation/Images/68747470733a2f2f692e6962622e636f2f684864445143772f53637265656e73686f742d66726f6d2d323032332d30312d32332d30302d34302d33372e706e67.png?raw=true" alt="Terminal">


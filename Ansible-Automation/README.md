## Windows

  - Build a Windows server (you can download predeployed windows 2016 ova from here: http://tinyurl.com/sol9vhc)
  
  I've created an EC2 instance from AWS so I can access from multiple devices.(with the right security group to allow outside connection)
  And a VMware Linux Ubuntu machine as the playbook runner. 
 
   Add Ansible user:
 <img src="https://i.ibb.co/0nfw4Z8/computer-manag.jpg" alt="Terminal">
 
   Add the user to the Administrator group:
 <img src="https://i.ibb.co/hXG0WLQ/ansible-add.jpg" alt="Terminal">

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
 Run Playbook:
 
<img src="https://i.ibb.co/wgP2cDB/Screenshot-from-2023-01-22-20-02-10.png" alt="Terminal">



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
 
<img src="https://i.ibb.co/hYpgb4Z/Screenshot-from-2023-01-22-20-10-05.png" alt="Terminal">

 
      
* Install dns service and create new zone(you can choose any domain name that you want)
 Add DNS install feature:
 
 ```
     - name: Install DNS
       win_feature:
         name: DNS
         state: present

 ```
 Run:
 
<img src="https://i.ibb.co/rdsdBmd/Screenshot-from-2023-01-22-20-19-53.png" alt="Terminal">


  - Add a record to point the local web server you created, also make sure to create a record to perform dns reverse lookup
  - Add a small exe file or a an image to the web site you created and download it via HTTP(not via HTTPS). Record(sniff) the download session into a pcap file.
  - Filter the download session from the pcap file and create a screenshot, describe the communication steps steps in the session

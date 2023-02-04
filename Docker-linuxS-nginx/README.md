## Docker

- Create a docker file to install linux server with nginx.
- Change the default port to 8080.
- Create an image out of it.
- Upload your docker script to your Git repo


Created a Dockerfile:

```
FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx && apt-get install curl -y


RUN rm -f /etc/nginx/sites-enabled/* 
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

EXPOSE 8080

CMD ["nginx"]

```
Build the image:

```
#docker build -t my-nginx-image .

```
Run and Shell into the docker file to change the default port to 8080:

```
#docker run -it --name 888nginx my-nginx-image /bin/bash
```
Port change:

<img src="https://github.com/DorBitton/888-DevOps-candidate-HS/blob/main/Docker-linuxS-nginx/Images/68747470733a2f2f692e6962622e636f2f56714d447768712f53637265656e73686f742d66726f6d2d323032332d30312d32332d30312d33392d31332e706e67.png?raw=true" alt="Terminal">

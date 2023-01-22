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

<img src="https://i.ibb.co/VqMDwhq/Screenshot-from-2023-01-23-01-39-13.png" alt="Terminal">

nginx site is loding while running in the container:


<img src="https://i.ibb.co/7Wk95kZ/Screenshot-from-2023-01-23-01-52-10.png" alt="Terminal">




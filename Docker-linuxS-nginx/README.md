## Docker

- Create a docker file to install linux server with nginx.
- Change the default port to 8080.
- Create an image out of it.
- Upload your docker script to your Git repo


```
FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx && apt-get install curl -y


RUN rm -f /etc/nginx/sites-enabled/* 
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

EXPOSE 8080

CMD ["nginx"]

#docker build -t my-nginx-image .

```

```
# docker run -it --name 888nginx my-nginx-image /bin/bash
```

 <img src="https://i.ibb.co/VqMDwhq/Screenshot-from-2023-01-23-01-39-13.png" alt="Terminal">

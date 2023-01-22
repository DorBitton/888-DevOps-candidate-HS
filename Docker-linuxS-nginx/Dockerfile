FROM ubuntu:latest

RUN apt-get update && apt-get install -y nginx && apt-get install curl -y


RUN rm -f /etc/nginx/sites-enabled/* 
RUN ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

EXPOSE 8080:8080

CMD ["nginx"]

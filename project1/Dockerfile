FROM ubuntu:22.04
RUN apt-get update
RUN apt-get install -y apache2

RUN echo "What the hell" > /var/www/html/index.html

EXPOSE 80

CMD ["apachectl", "-D", "FOREGROUND"]

# docker build -t cs325:copy .
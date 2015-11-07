FROM ubuntu:14.04
MAINTAINER clayton.kehoe@outlook.com

RUN apt-get update
RUN apt-get install -y git curl python

# Install pip
RUN /usr/bin/curl -o ./get-pip.py -L https://bootstrap.pypa.io/get-pip.py
RUN /bin/chmod 0755 ./get-pip.py
RUN ./get-pip.py

# Install python dependencies
RUN /usr/local/bin/pip install nose paste requests web.py

# Clone the taskcluster-api project repo
RUN /usr/bin/git clone https://github.com/ckehoe/taskcluster-api.git /var/lib/taskcluster-api

WORKDIR "/var/lib/taskcluster-api"
EXPOSE 80

# Start the built-in python web server
CMD [ "/usr/bin/python", "api.py", "80" ]

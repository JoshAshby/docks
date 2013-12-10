# RethinkDB
#
# VERSION 1

# use the ubuntu base image provided by dotCloud
FROM ubuntu

MAINTAINER Joshua Ashby joshuaashby@joshashby.com

# make sure the package repository is up to date
# and add the rethink ppa
RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get upgrade -y
RUN apt-get install -y python-software-properties

RUN add-apt-repository ppa:rethinkdb/ppa
RUN apt-get update

RUN apt-get install -y rethinkdb

# ALL THE PORTS
EXPOSE 28015 29015 8080

# create the /rethinkdb_data dir structure
# and make it a volume
RUN /usr/bin/rethinkdb create
VOLUME ["/rethinkdb_data"]

ENTRYPOINT ["/usr/bin/rethinkdb"]

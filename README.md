# taskcluster-api
A very simple API that will produce a JSON object containing each taskId and its state by invoking the mozilla taskcluster API. 

# How to use the API
The API returns a JSON object containing the taskIds and the associated status according to the graphId.  

#Sample Output
```bash
[
  {
    'taskId':'dgsdgsgsdgbt23gs', 
    'status':'Complete'
  },
  {
    'taskId':'sdgfn8932t2jompg',
    'status':'Complete'
  }
]
```

#API URI's
Option 1 - Returns the tasks and statuses based on the default graphId
```bash
http://localhost or http://localhost/tasks/status
```
Option 2 - Returns the tasks and statuses based on a custom graphId
```bash
http://localhost/tasks/status?graphId={graphId}
```
# Installation
There are two options for installing and running the taskcluster-api. 

## Docker
Can be installed on any platform that supports the Docker client.

Install Docker
```bash
http://docs.docker.com/engine/installation/
```
Start the docker service
```bash
sudo service docker start
```

Pull the image
```bash
docker pull ckehoe/taskcluster-api
```
Start the container on localhost port 80
```bash
docker run -p 80:80 -t -i ckehoe/taskcluster-api (add -d if you want it to run in the background)
```
Run curl against localhost to invoke the API (for additional options see "How to use the API")
```bash
curl http://localhost
```

## Puppet
The provided puppet script will download all required dependencies and start the API on localhost. It has been tested on Ubuntu 14.04 and the Amazon Linux AMI but should work for most version of linux.

### Download the Puppet Client

Debian
```bash
sudo apt-get update && sudo apt-get install -y puppet
```
RPM
```bash
sudo yum check-update && sudo yum install -y puppet
```

Start the puppet service
```bash
sudo service puppet start
```

cd to the puppet directory
```bash
cd taskcluster-api/deploy/puppet
```

Install and Deploy the taskcluster-api
```bash
sudo puppet apply --modulepath ./modules manifests/site.pp
```

Run curl against localhost to invoke the API (for additional options see "How to use the API")
```bash
curl http://localhost
```

# Testing
Use the nose module to test the application. Test scripts are located at taskcluster-api/tests/api_tests.py.

Go to the root of the taskcluster directory
```bash
cd {installation-location}/taskcluster-api
```
Run nosetests
```bash
WEBPY_ENV=test nosetests
```
# Any questions?
clayton.kehoe@outlook.com

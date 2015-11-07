# taskcluster-api
A very simple api that will produce a JSON object containing each taskId and it's state by invoking the mozilla taskcluster api. 

# How to use the API
*API Description*
The api returns a JSON object containing the taskIds and their status associated with a graphId.  

*Sample output*
{
  {
    'taskId':'dgsdgsgsdgbt23gs', 
    'status':'Complete'
  },
  {
    'taskId':'sdgfn8932t2jompg',
    'status':'Complete'
  }
}

*Using the api*

Option 1 - Return the tasks and statuses using the default graphId
http://localhost or http://localhost/tasks/status

Option 2 - Return the tasks and statuses using a custom graphId
http://localhost/tasks/status?graphId={graphId}

# How to install
*Installation*
There are two options for installing and running the taskcluster-api. 

*Docker*
Can be used on any platform that supports Docker

Install Docker
http://docs.docker.com/engine/installation/

Start the docker service
sudo service docker start

Pull the image
docker pull ckehoe/taskcluster-api

Start the container on localhost port 80
docker run -p 80:80 -t -i ckehoe/taskcluster-api (add -d if you want to run it in the background)

Run curl against localhost to invoke the api (for additional options see below)
curl http://localhost

*Puppet Deployment Script*
Warning - This script has been verified to work with a fresh installation of Ubuntu 14.04 and Amazon Linux. It should work just find on most unix-like operating systems (inluding Mac OS X) but if it doesn't then try the docker installation instead.

Install Puppet Client
Ubuntu
sudo apt-get install -y puppet

Redhat + Derivatives
sudo yum install -y puppet

Mac OS X
sudo brew install puppet

Start the Puppet Agent
sudo service puppet start

Run the deploy.pp script via puppet apply
puppet apply -l {log_file} taskcluster-api/deploy/puppet/deploy.pp

Run curl against localhost to invoke the api (for additional options see below)
curl http://localhost

# How to test
*Testing*
The application can easily be tested via nose. Test scripts are located at taskcluster-api/tests/api_tests.py.

Go to the root of the taskcluster directory
cd {installation-location}/taskcluster-api

Run Node tests
WEBPY_ENV=test nosetests

*Any questions?*
clayton.kehoe@outlook.com

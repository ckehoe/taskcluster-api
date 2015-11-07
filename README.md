# taskcluster-api
A very simple api that will produce a JSON object containing each taskId and it's state by invoking the mozilla taskcluster api. 

# How to use the API
The api returns a JSON object containing the taskIds and their status associated with a graphId.  

#Sample output*
```bash
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
```

#Using the api*
Option 1 - Return the tasks and statuses using the default graphId
```bash
http://localhost or http://localhost/tasks/status
```
Option 2 - Return the tasks and statuses using a custom graphId
```bash
http://localhost/tasks/status?graphId={graphId}
```
# How to install
There are two options for installing and running the taskcluster-api. 

# Docker
Can be used on any platform that supports Docker

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
docker run -p 80:80 -t -i ckehoe/taskcluster-api (add -d if you want to run it in the background)
```
Run curl against localhost to invoke the api (for additional options see below)
```bash
curl http://localhost
```

# How to test
The application can easily be tested via nose. Test scripts are located at taskcluster-api/tests/api_tests.py.

Go to the root of the taskcluster directory
```bash
cd {installation-location}/taskcluster-api
```
Run Node tests
```bash
WEBPY_ENV=test nosetests
```
# Any questions?
clayton.kehoe@outlook.com

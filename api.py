#!/usr/bin/python

import json
import os
import requests
import subprocess
import web

urls = (
    '/', 'index',
    '/tasks/status', 'index'
)

class index:
    def GET(self):
      api_metadata = {}
      tasks_object = {}
      task_statuses = {}

      # read from the config file to get the
      # graphId and base api url
      with open("conf/api.json", 'r') as api_data:
          api_metadata = json.loads(api_data.read())

      # if a graphId was passed with the request use it. If
      # not use the default graphId
      user_input = web.input()

      if "graphId" in user_input:
          graph_id = user_input.graphId
      else:
          graph_id = api_metadata['graphId']
          

      # make a request to the task cluster api
      try:
          request_obj = requests.get(os.path.join(api_metadata['baseUrl'], graph_id, 'inspect'))
      except:
          return json.dumps({"message": "error - unable to retrieve taskcluster api response"})

      # convert the response into a dictionary
      try:
          tasks_object = json.loads(request_obj.text)
      except:
          return json.dumps({"message": "error - unable to serialize taskcluster api response"})

      # Prepare the proper api response based off the data returned from the taskcluster api
      if "error" in tasks_object: # Check for error key in json object
          task_statuses = {"message": "error - taskcluster api call failed"}
      elif "tasks" in tasks_object: # Ensure tasks are returned
          for task in tasks_object['tasks']:
              if 'taskId' in task and 'state' in task: # Ensure that the task object is valid
                  task_statuses.update({task['taskId']:task['state']})
          
      if not task_statuses:
          task_statuses = {"message": "no tasks available for graphId {0}".format(graph_id)}
      
      return json.dumps(task_statuses)
      

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()

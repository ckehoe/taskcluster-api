#!/usr/bin/python

import json
import requests
import subprocess
import web

urls = (
    '/', 'index', 
    '/tasks/status', 'index', 
    '/tasks/status/pretty', 'html'
)
task_graph_id = 'O6pKa79XTaKDyDv5vGH51A'
task_cluster_url = 'https://scheduler.taskcluster.net/v1/task-graph/{0}/inspect'.format(task_graph_id)

class index:
    def GET(self):
      tasks_object = {}
      task_statuses = {}

      # make a request to the task cluster api
      request_obj = requests.get(task_cluster_url)
      tasks_object = json.loads(request_obj.text)

      # loop through each task and build a dictionary
      # of task id and status
      for task in tasks_object['tasks']:
          task_statuses.update({task['taskId']:task['state']})
      return json.dumps(task_statuses)
      

class html:
    def GET(self):
        return "Pretty HTML" 

if __name__ == "__main__": 
    app = web.application(urls, globals())
    app.run()

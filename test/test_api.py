#!/usr/bin/env python

import json
from paste.fixture import TestApp
from nose.tools import *
from api import app

class TestCode():
    def __init__(self):
        self.middleware = []
        self.api_metadata = {}
        self.testApp = TestApp(app.wsgifunc(*self.middleware))

        # read from the config file to get the
        # graphId and base api url
        with open("conf/api.json", 'r') as self.api_data:
            self.api_metadata = json.loads(self.api_data.read())
 
    # Test 1 - Accessing the root directory 
    # should redirect to /tasks/status
    def test_index(self):
        r = self.testApp.get('/')
        assert_equal(r.status, 200)
       
    # Test 2 - Accessing the normal api path should 
    # return a 200 header and return a valid JSON
    # object containing tasks ids and statuses
    def test_api_path_no_query_string(self):
        r = self.testApp.get('/tasks/status')
        assert_equal(r.status, 200)

    # Test 3 - Passing a valid graphId as a query
    # string should return a 200 header and return
    # a valid JSON object containing tasks ids and statuses
    def test_api_path_with_valid_graphId_query_string(self):
        r = self.testApp.get("/tasks/status?graphId={0}".format(self.api_metadata['graphId']))
        assert_equal(r.status, 200)

    # Test 4 - Passing an invalid graphId as a query
    # string should return a 200 and a valid JSON object
    # containing an error message
    def test_api_path_with_invalid_graphId_query_string(self):
        r = self.testApp.get("/tasks/status?graphId={0}".format(self.api_metadata['badGraphId']))
        assert_equal(r.status, 200)
        r.mustcontain('error')



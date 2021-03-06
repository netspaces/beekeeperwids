#!/usr/bin/python

import json
import os
import sys
import time
import traceback
import urllib2

from beekeeperwids.utils.errors import ErrorCodes as ec
from beekeeperwids.utils.rest import makeRequest

class WIDSClient:

    def __init__(self, address, port):
        self.address = address
        self.port = port

    def isActive(self):
        '''
        check if the WIDS server is up and responding to requests
        '''
        resource = '/active'
        (error,data) = makeRequest(self.address, self.port, resource)
        if error == None:
            return True
        else:
            return False

    def newRules(self):
        resource = '/rules/new'
        return makeRequest(self.address, self.port, resource)

    def addRule(self, rule_id, rule_name, rule_conditions, rule_actions):
        resource = '/rules/add'
        parameters = {'rid':rule_id, 'name':rule_name, 'conditions':rule_conditions, 'actions':rule_actions}
        return makeRequest(self.address, self.port, resource, parameters)

    def status(self):
        resource = '/status'
        return makeRequest(self.address, self.port, resource)

    def alerts(self):
        resource = '/alerts'
        return makeRequest(self.address, self.port, resource, {})

    def generateAlert(self, alert_name):
        resource = '/alerts/generate'
        return makeRequest(self.address, self.port, resource, {'alert_name':alert_name})

    def addDrone(self, ip, port):
        resource = '/drone/add'
        parameters = {'ip':ip, 'port':port}
        return makeRequest(self.address, self.port, resource, parameters)

    def delDrone(self, drone_index):
        resource = '/drone/delete'
        parameters = {'drone_index':drone_index}
        return makeRequest(self.address, self.port, resource, parameters)

    def taskDrone(self, droneIndexList, task_uuid, task_plugin, task_channel, task_parameters, module_index=None):
        resource = '/drone/task'
        parameters = {'droneIndexList':droneIndexList, 'uuid':task_uuid, 'channel':task_channel, 'plugin':task_plugin, 'parameters':task_parameters, 'module_index':module_index}
        return makeRequest(self.address, self.port, resource, parameters)

    def detaskDrone(self, droneIndexList, task_uuid):
        resource = '/drone/detask'
        parameters = {'droneIndexList':droneIndexList, 'uuid':task_uuid}
        return makeRequest(self.address, self.port, resource, parameters)

    def loadModule(self, name, settings):
        resource = '/module/load'
        parameters = {'name':name, 'settings':settings}
        return makeRequest(self.address, self.port, resource, parameters)

    def unloadModule(self, module_index):
        resource = '/module/unload'
        parameters = {'module_index':module_index}
        return makeRequest(self.address, self.port, resource, parameters)



#! /usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson as json, httplib, urllib, sys, os

class Plugin(indigo.PluginBase):

  def __init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs):
    indigo.PluginBase.__init__(self, pluginId, pluginDisplayName, pluginVersion, pluginPrefs)
    self.debug = True

  def __del__(self):
    indigo.PluginBase.__del__(self)


  def startup(self):
    self.debugLog(u"Plugin Initialized")

  def shutdown(self):
    self.debugLog(u"Plugin Disabled")

  # actions go here
  def send(self, pluginAction):
    connection = httplib.HTTPSConnection('api.parse.com', 443)
    connection.connect()
    connection.request('POST', '/1/push', json.dumps({
           "where": {
             "deviceType": "ios"
           },
           "data": {
             "alert": pluginAction.props["txtmessage"]
           }
         }), {
           "X-Parse-Application-Id": self.pluginPrefs["parseapikey"],
           "X-Parse-REST-API-Key": self.pluginPrefs["restkey"],
           "Content-Type": "application/json"
         })
    self.debugLog(u"Sent message to parse.com")
from ferris import Controller, route, scaffold, ndb, localize, settings, Model
from google.appengine.api import urlfetch, users
import base64
import json
from datetime import datetime, timedelta
from apiclient.discovery import build
from apiclient import errors
from ferris.core import oauth2
from ferris.core import google_api_helper
import httplib2

class Home(Controller):
    class Meta:
        components = (scaffold.Scaffolding,)#oauth.OAuth,
        Model=(Model)

    def list(self):
        """
        Shows the list of apps to which the current use has access to
        """
        
        self.context['home'] = "Welcome to ferris"


    
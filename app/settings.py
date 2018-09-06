"""
This file is used to configure application settings.

Do not import this file directly.

You can use the settings API via:

    from ferris import settings

    mysettings = settings.get("mysettings")

The settings API will load the "settings" dictionary from this file. Anything else
will be ignored.

Optionally, you may enable the dynamic settings plugin at the bottom of this file.
"""

settings = {}

settings['timezone'] = {
    'local': 'US/Eastern'
}

settings['email'] = {
    # Configures what address is in the sender field by default.
    'sender': None
}

settings['app_config'] = {
    'webapp2_extras.sessions': {
        # WebApp2 encrypted cookie key
        # You can use a UUID generator like http://www.famkruithof.net/uuid/uuidgen
        'secret_key': '',
    }
}


settings['upload'] = {
    # Whether to use Cloud Storage (default) or the blobstore to store uploaded files.
    'use_cloud_storage': True,
    # The Cloud Storage bucket to use. Leave as "None" to use the default GCS bucket.
    # See here for info: https://developers.google.com/appengine/docs/python/googlecloudstorageclient/activate#Using_the_Default_GCS_Bucket
    'bucket': None
}

# Enables or disables app stats.
# Note that appstats must also be enabled in app.yaml.
settings['appstats'] = {
    'enabled': False,
    'enabled_live': False
}

settings['oauth2'] = {
    # OAuth2 Configuration should be generated from
    # the google cloud console (Credentials for Web Application)
    'client_id': '',
    'client_secret': '',
    'developer_key': None  # Optional
}

settings['oauth2_service_account'] = {
    # OAuth2 service account configuration should be generated
    # from the google cloud console (Service Account Credentials)
    'client_email':'',
    'private_key': """""",  # Must be in PEM format
    'developer_key': None  # Optional
}


settings['api'] = {
    'api_key': ''
}

"""Resource APIs Config"""
settings["resource"] = { # here goes my resource name
    "active_env": "prod", #prod, test, dev. Use this variable to switch between environments on resource
    "api_key":"",
    "username":"",
    "password":"",
    "Authorization":"Basic",
    "Content-Type":"application/json",
    "headers":["Authorization", "Content-Type"]
}

settings["resource"]["api"] = {
    "resource_name":"resource-url",
}


# Optionally, you may use the settings plugin to dynamically
# configure your settings via the admin interface. Be sure to
# also enable the plugin via app/routes.py.

import plugins.settings
#import plugins.service_account.settings
# import any additional dynamic settings classes here.


# Un-comment to enable dynamic settings
plugins.settings.activate(settings)

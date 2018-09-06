"""
Central place to store event listeners for your application,
automatically imported at run time.
"""
import logging, json
from ferris.core.events import on
from google.appengine.api import users
from datetime import datetime, timedelta
from ferris import settings

def domain_chain(controller):
    """
    Make sure the active user's email account falls within the accepted domains.
    """
    if controller.route.prefix == 'cron':
        return True
      
    elif controller.route.prefix == 'api':
        if controller.request.GET.get('api_key') == settings.get('api', {}).get('api_key'):
            return True
        else: 
            return False

    else:
        user = users.get_current_user()
        if not user:
            return controller.redirect(users.create_login_url('/'))
        else:
            return True

  

@on('controller_before_authorization')
def inject_authorization_chains(controller, authorizations):
    if controller.route.prefix != 'do':
        authorizations.insert(0, domain_chain)


"""
@on('controller_before_render')
def before_render(controller):
    if controller.route.prefix != 'do' and controller.route.prefix != 'api':  
"""
    
    
    
    
    
    
    
    


from ferris.core import routing, plugins
from ferris.controllers.download import Download

# Routes all App handlers
routing.auto_route()

# Default root route
#routing.default_root()
routing.redirect('/', to='/home')


# Used for downloading files
routing.route_controller(Download)


# Plugins
plugins.enable('settings')
plugins.enable('service_account')
plugins.enable('oauth_manager')

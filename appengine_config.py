from ferris import fix_imports
from ferris.core import settings
from google.appengine.ext import vendor

(fix_imports)
settings.load_settings()

#vendor.add('lib')

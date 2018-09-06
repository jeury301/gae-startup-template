
from ferris import Controller, route_with

class SanityCheck(Controller):
    class Meta:
        prefixes = ('do' , 'cron')

    @route_with('/do/sanity-check')
    def do_sanity_check(self):
        return 200
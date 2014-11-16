# Entry point for Countdown Server
#

import timermanager
import web

urls = (
    '/test', 'test',
    '/status', 'status',
    '/list', 'timer_list'
)

class test:
    """The controller for testing purposes. TODO remove from production code"""
    def GET(self):
        msg = 'testing...'
        manager = timermanager.TimerManager()
        msg += '\nManager Object Info: ' + manager.get_info()
        msg += '\nManaged timers: ' + ', '.join(manager.get_timers())
        return msg

class status:
    """Handles /status requests. Provides actual server status."""
    def GET(self):
        result = {'status': 'OK'}
        return result


class timer_list:
    """Handles /lists requests. Returns a detailed timers list."""
    def GET(self):
        timers = [{'id': 23, 'name': 'Work'}, { 'id': 34, 'name': 'Break' } ]
        return timers

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


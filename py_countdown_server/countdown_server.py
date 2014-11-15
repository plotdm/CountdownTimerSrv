# Entry point for Countdown Server
#

import timer_manager
import web

urls = (
    '/test', 'test',
    '/status', 'status',
    '/list', 'timer_list'
)

#
# @class test
# A controller for testing purposes
#
class test:
    def GET(self):
        msg = 'testing...'
        manager = timer_manager.timer_manager()
        msg += '\nManager Object Info: ' + manager.getInfo()
        msg += '\nManaged timers: ' + ', '.join(manager.getTimers())
        return msg

#
# @class status
# Handles /status requests. Provides actual server status.
#
class status:
    def GET(self):
        result = {'status': 'OK'}
        return result


#
# @class timer_list
# Handles /list requests. Returns a detailed timers list.
#
class timer_list:
    def GET(self):
        timers = [{'id': 23, 'name': 'Work'}, { 'id': 34, 'name': 'Break' } ]
        return timers

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()


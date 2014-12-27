#!/usr/bin/python
# -*- coding: utf-8 -*-

# Entry point for Countdown Server
#

import json
import logging
import timer
import timermanager
import web

urls = (
    '/status', 'status',
    '/list', 'timer_list',
    '/list/details', 'timer_list_details',
    '/timer/(.+)', 'get_timer',
    '/new', 'new_timer',
    '/delete/(.+)', 'delete_timer'
)

def jsonEncodeTimers(timers):
    return json.dumps(timers, cls=timer.TimerJSONEncoder)

timer_manager = timermanager.TimerManager()

class status:
    """Handles /status requests. Provides actual server status."""
    def GET(self):
        result = {'status': 'OK'}
        return result

class timer_list:
    """Handles /list requests. Returns a detailed timers list."""
    def GET(self):
        timers = timer_manager.get_timers()
        return jsonEncodeTimers(timers)


class timer_list_details:
    """Handles /list/details request. Returns a details timer list."""
    def GET(self):
        list_request = timer_list()
        return list_request.GET()

class get_timer:
    """Handles /timer?id= request. Returns details of the timer with spedified ID."""
    def GET(self, id):
        id = int(id)
        tmr  = timer_manager.get_timer(id)
        return jsonEncodeTimers(tmr)

class new_timer:
    """Handles /new request. Creates a new timer and returns its details."""
    def GET(self):
        name = web.input().name
        duration = int(web.input().duration)

        new_tmr = timer_manager.create_timer(name, int(duration))
        return jsonEncodeTimers(new_tmr)
        
class delete_timer:
    """Handles /delete request. Deletes the timer with specified ID."""
    def GET(self, id):
        id = int(id)
        timer_manager.delete_timer(id)
        return {'status': 'OK'}

if __name__ == "__main__":
    logging.basicConfig(filename="countdownserver.log", level=logging.DEBUG)
    logging.info('countdown server started')
    app = web.application(urls, globals())
    app.run()


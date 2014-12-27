import datetime
import json
import timerstate

class Timer(object):
    """Representds a timer instance. Objest of the class are used
    for controlling timer's behavior.
    """
    
    def __init__(self, id, name, duration):
        """Initializes the timer."""
        self.id = id
        self.name = name
        self.duration = duration
        self.state = timerstate.TimerState()

    def start(self):
        """Starts the timer."""
        now_time = datetime.datetime.now()
        if self.state.pause_time is None:
            self.state.end_time = now_time + datetime.timedelta(milliseconds=self.duration)
        else:
            self.state.end_time = now_time + self.state.end_time - self.state.pause_time
        self.state.is_running = True 
    def stop(self):
        """Stops the timer."""
        self.state.end_time = None
        self.state.pause_time = None
        self.state.is_running = False

    def pause(self):
        """Pauses the timer."""
        self.state.pause_time = datetime.datetime.now()
        self.state.is_running = False

    def is_running(self):
        """Checks whether the timer is running.
        Returns True if the timer is running, False otherwise."""
        return self.state.is_running

class TimerJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Timer):
            return { "id": obj.id,
                     "name": obj.name,
                     "duration": obj.duration,
                     "state": timerstate.TimerStateJSONEncoder.timer_state_dictionary(obj.state) }
        else:
            return super(TimerJSONEncoder, self).default(obj)


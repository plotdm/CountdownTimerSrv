import json

class TimerState:
    """Represents a timer's state."""

    def __init__(self):
        self.is_running = False
        self.pause_time = None
        self.end_time = None

class TimerStateJSONEncoder(json.JSONEncoder):
    @staticmethod
    def timer_state_dictionary(obj):
        return { "is_running": obj.is_running,
                 "end_time": obj.end_time,
                 "pause_time": obj.pause_time }
        
    def default(self, obj):
        if isinstance(obj, TimerState):
            return TimerStateJSONEncoder.timer_state_dictionary(obj)
        else:
            return super(TimerStateJSONEncoder, self).default(obj)

import logging
import timer

class TimerManager(object):
    """Manages countdown timers."""

    def __init__(self):
        self.timers = []
        self.last_id = 0

    def get_timers(self):
        """Returns a list of timers."""
        return self.timers

    def get_timer(self, id):
        """Returns the timer with specified ID.
        Arguments:
        id -- The ID that identifies the timer.
        """
        for t in self.timers:
            if t.id == id:
                return t
        return None

    def create_timer(self, name, duration):
        """Creates a timer with specified name and returns its instance.
        Arguments:
        name -- The name of the timer.
        duration -- The timer's duration, seconds (number)
        Returns:
        An  instance of the timer.
        """
        tmr = timer.Timer(self.last_id, name, duration)
        self.timers.append(tmr)
        self.last_id += 1
        return tmr

    def delete_timer(self, id):
        """Deletes the timer with specified ID.
        Arguments:
        id -- The ID that identifies the timer.
        """
        for t in self.timers:
            logging.debug('deleting id {0}, having id {1}'.format(id, t.id))
            if t.id == id:
                logging.debug('we are here')
                self.timers.remove(t)
                break

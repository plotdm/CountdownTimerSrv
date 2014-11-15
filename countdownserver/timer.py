#
# @class Timer
# Represents a timer instance. Used to control timer's behaviour.
#
class Timer:
    #
    # @method __init__
    # Initializes the timer.
    #
    def __init__(self):
        self._is_running = False

    #
    # @method start
    # Starts the timer.
    #
    def start(self):
        self._is_running = True

    #
    # @method stop
    # Stops the timer.
    #
    def stop(self):
        self._is_running = False

    #
    # @method is_running
    # Checks whether the timer is running.
    # @return True if the timer is running, false otherwise.
    #
    def is_running(self):
        return self._is_running

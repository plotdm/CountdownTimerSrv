class Timer:
    """Representds a timer instance. Objest of the class are used
    for controlling timer's behavior.
    """

    def __init__(self):
        """Initializes the timer."""
        self._is_running = False

    def start(self):
        """Starts the timer."""
        self._is_running = True

    def stop(self):
        """Stops the timer."""
        self._is_running = False

    def is_running(self):
        """Checks whether the timer is running.
        Returns True if the timer is running, False otherwise."""
        return self._is_running

import os, sys
import unittest

countdownserver_path = os.path.abspath('../countdownserver')
sys.path.append(countdownserver_path)
import timer

class TimerTests(unittest.TestCase):
    def test_timer_is_running(self):
        t = timer.Timer();
        self.assertFalse(t.is_running())
        t.start()
        self.assertTrue(t.is_running())
        t.stop()
        self.assertFalse(t.is_running())

if __name__ == '__main__':
    unittest.main()
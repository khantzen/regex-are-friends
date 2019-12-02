import regex
import unittest


# a|b will match a OR b
class ConditionnalAndLoopTest(unittest.TestCase):
    def test_pipe_work_as_or(self):
        pattern = r'your regex here'
        assert regex.match(pattern, 'liskov')
        assert regex.match(pattern, 'noether')

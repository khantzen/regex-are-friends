import regex
import unittest


class ConditionnalAndLoopTest(unittest.TestCase):

    # a|b will match a OR b
    def test_pipe_work_as_or(self):
        pattern = r'liskov|noether'
        assert regex.match(pattern, 'liskov')
        assert regex.match(pattern, 'noether')

if __name__ == '__main__':
    unittest.main()

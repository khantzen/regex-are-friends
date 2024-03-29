import regex
import unittest


class ConditionalAndLoopTest(unittest.TestCase):

    # a|b will match a OR b
    def test_pipe_work_as_or(self):
        pattern = r'your regex here'
        assert regex.match(pattern, 'liskov')
        assert regex.match(pattern, 'noether')

    # a{n} will match a n times
    def test_acollade_match_the_value_n_time(self):
        pattern = r'your regex here'
        assert regex.match(pattern, 'kkkkk')

    # a{,n} will match a maximum n times
    def test_acollade_with_coma_match_value_at_max_n_times(self):
        pattern = r'your regex here'
        assert regex.match(pattern, 'e')
        assert regex.match(pattern, 'ee')
        assert regex.match(pattern, 'eee')
        assert regex.match(pattern, 'eeee')
        assert regex.match(pattern, 'eeeee')
        assert not regex.match(pattern, 'eeeeee')

    def test_acollade_with_coma_match_value_at_max_n_times_2(self):
        pattern = r'your regex here'
        assert regex.match(pattern, '-')
        assert regex.match(pattern, '-_')
        assert regex.match(pattern, '-_-')
        assert regex.match(pattern, '-_-"')
        assert regex.match(pattern, '-_-"/')
        assert not regex.match(pattern, r'-_-"/\-_-')


if __name__ == '__main__':
    unittest.main()

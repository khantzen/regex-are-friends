import regex
import unittest


class simpleMatchTest(unittest.TestCase):
    # one letter should match itself
    def test_letter_should_math_a_letter(self):
        pattern = r'c'
        assert regex.match(pattern, "c")

    # . should match any character
    def test_dot_should_match_any_character(self):
        pattern = r'.'
        assert regex.match(pattern, "a")
        assert regex.match(pattern, "c")
        assert regex.match(pattern, "*")

    # \w should match letter number and underscore
    def test_w_should_match_letter_number_and_underscore(self):
        pattern = r'\w'
        assert regex.match(pattern, "a")
        assert regex.match(pattern, "C")
        assert regex.match(pattern, "_")
        assert regex.match(pattern, "5")

    # \W should match any character that is not matched by \w
    def test_W_should_match_any_character_not_matched_by_w(self):
        pattern = r'\W'
        assert regex.match(pattern, "-")
        assert regex.match(pattern, "(")
        assert regex.match(pattern, "@")
        assert regex.match(pattern, "+")

    # \d should match any number
    def test_d_should_match_any_number(self):
        pattern = r'\d'
        assert regex.match(pattern, '5')

    # pattern character position should match string character position
    def test_pattern_character_position_should_match_string_character_at_the_same_position(self):
        pattern = r'\d\W'
        assert regex.match(pattern, '5+')
        assert regex.match(pattern, '2-')

    def test_pattern_character_position_should_match_string_character_at_the_same_position_2(self):
        pattern = r'a\D\w'
        assert regex.match(pattern, 'aF_')
        assert regex.match(pattern, 'a)_')


if __name__ == '__main__':
    unittest.main()

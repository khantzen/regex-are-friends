import regex
import unittest

line_break = '\n'


class LessSimpleMatchTest(unittest.TestCase):
    # anything between [] can match
    def test_anything_in_array_can_be_matched(self):
        pattern = r'your regex here'
        assert regex.match(pattern, 'a')
        assert regex.match(pattern, ')')

    # ^ mark the line begining
    def test_circonflex_mark_a_starting_line(self):
        pattern = r'your regex here'
        str_to_match = "a" + line_break + "b" + line_break + "c"
        assert regex.match(pattern, str_to_match)

    def test_circonflex_mark_a_starting_line_2(self):
        pattern = r'your regex here'
        str_to_match = "~8" + line_break + "_9" + line_break + "-6"
        assert regex.match(pattern, str_to_match)

    # () capture the matched result
    def test_parenthesis_capture_the_matched_result(self):
        pattern = r'your regex here'
        str_to_search_in = "defdf349,;:abckfifk<àç'"
        search = regex.search(pattern, str_to_search_in)
        assert search[0] == "abc"

    # (?<name> ) give a name to the capturing group
    def test_naming_capturing_group(self):
        pattern = r'your regex here'
        str_to_search_in = "dkjg_'_123abcofdo"
        search = regex.search(pattern, str_to_search_in)

        assert search['number'] == '123'
        assert search['letter'] == 'abc'

    def test_group_can_capture_more_than_one_time(self):
        pattern = r'your regex here'
        str_to_search_in = "aaa43hdf64kjdf90"

        search = regex.finditer(pattern, str_to_search_in)
        search_result = [match['two_digits'] for match in search]

        assert search_result == ['43', '64', '90']

    # $ mark the end of the line
    def test_dollar_mark_the_end_of_the_line(self):
        pattern = r'your regex here'

        first_str_to_search_in = "1234567890"
        second_str_to_search_in = "abde32"

        search_1 = regex.search(pattern, first_str_to_search_in)
        search_2 = regex.search(pattern, second_str_to_search_in)

        assert search_1['last_number'] == '90'
        assert search_2['last_number'] == '32'

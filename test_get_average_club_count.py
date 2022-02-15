"""A3. Test cases for function club_functions.get_average_club_count.
"""

import unittest
import club_functions


class TestGetAverageClubCount(unittest.TestCase):
    """Test cases for function club_functions.get_average_club_count.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_01_one_person_one_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_02_one_person_few_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association', 'Gym Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 2.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
  
    def test_03_one_person_few_clubs(self):
        param = {'Claire Dunphy': []}
        actual = club_functions.get_average_club_count(param)
        expected = 0.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
        
    def test_04_few_person_few_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association','gym'],\
                 'Kimmy Gibbler': ['Rock N Rollers']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_05_few_person_with_empty_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association','gym','study'],\
                 'Kimmy Gibbler': [],\
                 'Jesse Katsopolis': ['Parent Council']}
        actual = club_functions.get_average_club_count(param)
        expected = 1.5
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)

    def test_06_few_person_few_clubs(self):
        param = {'Claire Dunphy': ['Parent Teacher Association','gym','study'],\
                 'Kimmy Gibbler': ['Reading Club','Cooking Club', 'Bussiness'],\
                 'Jesse Katsopolis': ['Parent Council','Business','Reading'],\
                 'Leondra Moon': ['Knit Club', 'Business', 'Programming']}
        actual = club_functions.get_average_club_count(param)
        expected = 3.0
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
        
    def test_07_many_person_many_club(self):
        param = {'Claire Dunphy': ['Parent Teacher Association','gym','study'],\
                 'Kimmy Gibbler': ['Reading','Arts Club','Cooking','Study'],\
                 'Jesse Katsopolis': ['Parent Council'],\
                 'Carly Simon': ['Parent Teacher Association', 'Math Club'\
                                 'Programming Club', 'Economics Club', \
                                 'Volunteer Club', 'Photographing Club']}
        actual = club_functions.get_average_club_count(param)
        expected = 3.25
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertAlmostEqual(actual, expected, msg=msg)
    
    def test_mutation(self):
        param = {'Claire Dunphy': ['Parent Teacher Association','gym'],\
                 'Kimmy Gibbler': ['Rock N Rollers']}
        club_functions.get_last_to_first(param)
        expected = {'Claire Dunphy': ['Parent Teacher Association','gym'],\
                 'Kimmy Gibbler': ['Rock N Rollers']}
        msg = "Expected {}, but returned {}".format(expected, param)
        self.assertEqual(param, {'Claire Dunphy': \
                                 ['Parent Teacher Association','gym'],
                 'Kimmy Gibbler': ['Rock N Rollers']}, msg)  

if __name__ == '__main__':
    unittest.main(exit=False)


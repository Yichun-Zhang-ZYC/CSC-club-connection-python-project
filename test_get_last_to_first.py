"""A3. Test cases for function club_functions.get_last_to_first.
"""

import unittest
import club_functions


class TestGetLastToFirst(unittest.TestCase):
    """Test cases for function club_functions.get_last_to_first.
    """

    def test_00_empty(self):
        param = {}
        actual = club_functions.get_last_to_first(param)
        expected = {}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_01_one_person_one_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_02_one_person_few_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy', 'Bell Duphy','Steven Duphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil','Bell','Steven']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_03_one_person_one_friend_different_last(self):
        param = {'Clare Dunphy': ['Pual White']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'White': ['Pual']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_04_one_person_no_friend(self):
        param = {'Clare Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)
        
    def interchanged_friends(self):
        param = {'Clare Dunphy': ['Abby Moon'], 'Abby Moon': ['Clare Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Moon': ['Abby']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)        
        
    def test_05_few_person_same_friend_same_last(self):
        param = {'Clare Dunphy': ['Phil Dunphy'], \
                 'Ellen Dunphy':['Phil Dunphy'],\
                 'Steven Dunphy': ['Phil Dunphy']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil', 'Ellen', 'Steven']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)

    def test_06_few_person_different_friend_differnet_last(self):
        param = {'Clare Dunphy': ['Phil Dell'], \
                 'Ellen Jobs':['Phil Dell'],\
                 'Steven Mike': ['Scarlett Smith']}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare'], 'Dell': ['Phil'],\
                    'Mike': ['Steven'], 'Jobs': ['Ellen'], \
                    'Smith': ['Scarlett']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
        
    def test_07_normal_simple_case(self):
        param = {'Clare Dunphy': ['Allen Cornell', 'Ellen Cornell'], \
                 'Ellen Cornell':['Phil Dunphy', 'Lily Johnson'],\
                 'Steven Dunphy': []}
        actual = club_functions.get_last_to_first(param)
        expected = {'Dunphy': ['Clare', 'Phil', 'Steven'], \
                    'Cornell': ['Ellen', 'Allen'], 'Johnson': ['Lily']}
        msg = "Expected {}, but returned {}".format(expected, actual)
        self.assertEqual(actual, expected, msg)    
       
       
    def test_08_mutation(self):
        param = {'Clare Dunphy': ['Pual White']}
        club_functions.get_last_to_first(param)
        expected = {'Clare Dunphy': ['Pual White']}
        msg = "Expected {}, but returned {}".format(expected, param)
        self.assertEqual(param, {'Clare Dunphy': ['Pual White']}, msg)        


if __name__ == '__main__':
    unittest.main(exit=False)
   
   

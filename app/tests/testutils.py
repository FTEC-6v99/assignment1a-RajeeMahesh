# Create a unit test method to test the calculate_avg function created in the utils module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios

import unittest 
from app.src.utils import avg_calc

class TestUtils(unittest.testcase):
    def test_avg_cal_correct(self):

        input = [1,2,3,4,5]
        actual = avg_calc(input)
        expect = 3
        self.assertEqual(expect, actual)
        self.assertTrue(isinstance(actual,float))
    
    def test_avg_cal_empty(self):
        self.assertRaises(Exception, avg_calc, []) 

        

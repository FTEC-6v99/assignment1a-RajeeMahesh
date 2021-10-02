# Use unittest library to create a unit test method to test the calculate_avg_grade function created in the gradecalc module
# Make sure you include multiple unit tests to test that the function acts as expected in different scenarios
import unittest
from app.src.gradecalc import cal_avg_grade
from app.src.Student import Student
from app.src.Person import Person

class TestGradeCalc(unittest.TestCase):
    def test_avg_calc_correct(self):
        input = [Student('ram', 21, 34, 45.6), 
                 Student('dany', 23, 56, 90.8),
                 Student('dany', 23, 56, 87.8),
                 Student('moni', 22, 12, 91.5),
                 Student('ram', 21, 34, 76.9)
                 ]
        expect = {
             34: 61.25,
             56: 89.3,
             12: 91.5
         }

        
        actual = cal_avg_grade(input)
        self.assertTrue(isinstance(actual, dict))
        self.assertTrue(len(actual) == 3)
        self.assertFalse(len(actual) == 2)
        self.assertEqual(expect, actual)

    def test_avg_cal_empty(self):
        input = {}
        actual = cal_avg_grade(input)
        self.assertTrue(actual == {})

        
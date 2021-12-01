import unittest
from main.reto import *

input = 'TestCase.txt'
output = 'TestCase.txt'


class MyFirstTests(unittest.TestCase):
    def test_reto(self):
        self.assertEqual(run(input_file_name=input), outputData(output_file_name=output))

import unittest
import unittest.mock
from Day1_Exercise2 import Person
import sys
from io import StringIO

class TestPersonClass(unittest.TestCase):
    person1 = Person("Margaret", 45, "Salesperson")
    person2 = Person("Alex", 15)

    def test_adult(self):
        self.assertTrue(self.person1.is_adult(), "Function is_adult not working...")

    def test_age_retrieval(self):
        self.assertEqual(self.person1.age, 45, "Age retrieval not working...")

    def test_greet(self):
        self.assertMultiLineEqual(self.person1.greet(), "Hello, my name is Margaret and I am 45 years old.")

    def test_occupation_employed(self):
        self.assertMultiLineEqual(self.person1.introduce_occupation(), "I work as a Salesperson.", "Occupation retrieval for employed person not working...")

    def test_occupation_unemployed(self):
        self.assertMultiLineEqual(self.person2.introduce_occupation(), "I am Unemployed.", "Occupation retrieval for unemployed person not working...")

    def test_greeting_being_printed(self):
        terminal_output = StringIO()
        sys.stdout = terminal_output
        self.person1.greet()
        sys.stdout = sys.__stdout__
        self.assertMultiLineEqual("Hello, my name is Margaret and I am 45 years old.\n", terminal_output.getvalue())
        
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_greeting_being_printed_with_mock(self, mock_stdout):
        self.person1.greet()
        self.assertMultiLineEqual("Hello, my name is Margaret and I am 45 years old.\n", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
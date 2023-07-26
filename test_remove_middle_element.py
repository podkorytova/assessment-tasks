import unittest
import subprocess


class TestRemoveMiddleElement(unittest.TestCase):
    def test_three_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py", "-l", "9", "8", "7"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, '97')

    def test_two_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py", "-l", "9", "8"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, '8')

    def test_one_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py", "-l", "9"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, 'Yourlistisempty')

    def test_even_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py", "-l", "9", "8", "7", "6"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, '986')

    def test_odd_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py", "-l", "9", "8", "7", "6", "5"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, '9865')

    def test_zero_elements_in_list(self):
        result = subprocess.run(["python3.11", "code_remove_middle_element.py"], text=True, capture_output=True)
        result = result.stdout.replace('\n', '').replace(' ','')
        self.assertEqual(result, 'Yourlistisempty')


if __name__ == '__main__':
    unittest.main()

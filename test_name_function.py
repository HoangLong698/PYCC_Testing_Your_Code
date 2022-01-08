import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Test for 'name_function.py'."""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')
    
    def test_first_middle_last_name(self):
        # Do names like 'Long Huu Hoang Tran? '
        formatted_name = get_formatted_name('Long', 'Tran', 'Huu Hoang')
        self.assertEqual(formatted_name, 'Long Huu Hoang Tran')

if __name__ == '__main__': # is used to execute this block code only if the file was run directly, and not imported.
    unittest.main()
else:
    print("Execute when this module imported.")
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.employee = Employee('Long', 'Tran', 10000)
        # return super().setUp()
    
    def test_give_default_raise(self):
        self.employee.give_raise()
        # print(self.employee.annual_salary)
    
    def test_give_custom_raise(self):
        self.employee.give_raise(1000)
        print(f"{self.employee.first_name} {self.employee.last_name} has {self.employee.annual_salary} annual salary")
        # print(self.employee.annual_salary)

if __name__ == '__main__':
    unittest.main()
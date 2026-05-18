#write a test file for employee.py
#test _give_default_raise() and _give_custom_raise()

import pytest
from employee import Employee

@pytest.fixture
def employee():
    """Create a new employee for use in all test methods."""
    return Employee('John', 'Doe', 50000)   

def test_give_default_raise(employee):
    """Test that the default raise is $5000."""
    employee.give_raise()
    assert employee.annual_salary == 55000 
    
def test_give_custom_raise(employee):
    """Test that a custom raise works."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
    

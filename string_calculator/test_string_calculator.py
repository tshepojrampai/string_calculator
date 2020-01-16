import string_calculator as calc
import pytest


 
def test_one_integer():
    assert calc.add("")== 0

def test_one_number():
    assert calc.add("1") == 1
    
def test_two_number():
    assert calc.add("1,1") == 2
    assert calc.add("1,2,3,4")== 10
    assert calc.add("1,2,3,4,5")== 15

def test_new_line_and_commas(): 
    assert calc.add("1\n2,3")==6

def test_delimiters():
    assert calc.add("//;\n1;2")==3
    assert calc.add("//4\n142")

def test_delimiterrs():
    with pytest.raises(Exception) as err:
        assert add("-1,-2,3,4")
        str(err.value) == "-numbers not allowed! -1, -2."
# def test_1000_add():
#      assert calc.add("//;\n1001,1;2") == 2
def test_diff_delimiters():
    assert calc.add("//***\n1***2***3") == 6
    
# def test_moreDiff_delimiters():
    # assert calc.add("//[:D][%]\n1:D2%3") == 6
    # assert calc.add("//[***][%%%]\n1***2%%%3") == 6
    # assert calc.add("//[(-_-')][%]\n1(-_-')2%3") == 6
    # assert calc.add("//[abc][777][:(]\n1abc27773:(1") == 7


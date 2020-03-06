import string_calculator as calc
import pytest

def test_ints_passed_as_strings():
    assert calc.add("")== 0
    assert calc.add("1") == 1
    assert calc.add("1,1") == 2
    
def multiple_integers():
    assert calc.add("1,2,3,4")== 10
    assert calc.add("")== 0
    assert calc.add("1") == 1
    assert calc.add("1,1") == 2

def test_new_line_and_commas(): 
    assert calc.add("1\n2,3")==6

def test_delimiters():
    assert calc.add("//;\n1;2")== 3
    assert calc.add("//;\n1;2") == 3

def test_delimiterrs():
    with pytest.raises(Exception) as err:
        assert calc.add("-1,-2,3,4")
        str(err.value) == "-numbers not allowed! -1, -2."
def test_more_1000():
    assert calc.add("//;\n1000,1;2") == 3

def test_diff_delimiters():
    assert calc.add("//***\n1***2***3") == 6
def test_moreChar_delim():
    assert(calc.add("//[*][%]\n1*2%+???++@aqw^^^\\^3") == 6)
    
def test_diffAnylength_delim():
    assert(calc.add("//[:D][%]\n1:D2%3") == 6)
    assert(calc.add("//[**][%%%]\n1**2%%%3") == 6)
    assert(calc.add("//[(--')][%]\n1(--')2%3") == 6)    
def test_moreDiff_delimiters():
    assert calc.add("//[:D][%]\n1:D2%3") == 6
    assert calc.add("//[***][%%%]\n1***2%%%3") == 6
    assert calc.add("//[(-_-')][%]\n1(-_-')2%3") == 6
    assert calc.add("//[(-_-')][%]\n1(-_-')3%3") == 7
    


# any pytest file should start with "test_" or end with "_test"
#  any pytest function (metods) should start with "test_"
# any code should be wraped in methods
"""assert refers to the standard Python assert statement, 
which is used to verify conditions within your test code. 
pytest leverages and enhances this built-in assert statement 
for its assertion mechanism."""
# -k is used to run specific test cases
# -v is used to get more detailed information about the test execution
# -s is used to display print statements in the output
# you can mark (tag) @pytest.mark.smoke to run specific group of test cases
# u can skip test with @pytest.mark.skip
# you can use @pytest.mark.xfail to mark a test as expected to fail

import pytest

@pytest.mark.smoke
#@pytest.mark.skip
def test_firstProgarm():
    msg = "Hello World"
    assert msg == "World" , "Test Failed because strings do not match"


#
def test_MatchProgarm():
    a = 5
    b = 6
    assert a + b == 11, "Test Failed because values do not match"

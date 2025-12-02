""" fixtures are functions that provide a defined, reliable, 
and consistent context for tests. They are used to set up prerequisites for tests, 
such as initializing data, creating objects, 
establishing connections, or configuring environments.
Fixtures also handle the teardown or cleanup operations after tests are executed."""

# fixture areused to setup and teardown methods for test cases. 
#conftest.py is general file name for fixture file



import pytest


def test_example1(setup):
    print("Executing Test Example 1")
    
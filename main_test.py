"""
Unit tests for main.py
"""

import main

"""
Validate the name of the module is main
"""
def test_main_name() -> None:
    assert(main.__name__ == 'main')


"""
Validate the function named main exists
"""
def test_main_function()-> None:
    assert(getattr(main, 'main'))

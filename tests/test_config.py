# -*- coding: utf-8 -*-
"""py.test tests on main.py

.. moduleauthor:: Mathew Topper <mathew.topper@tecnalia.com>
"""

from polite.configuration import Config


def test_make_head_foot_bar():

    '''Test the length of the character strings matches input'''

    head_foot_length = 50
    head_title = 'This is a TEST!'

    header, footer = Config.make_head_foot_bar(head_title, head_foot_length)

    assert len(header) == head_foot_length
    assert len(footer) == head_foot_length



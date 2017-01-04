# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:24:33 2016

@author: 108630
"""

import abc

import pytest

from polite.abc import abstractclassmethod


class ClassBase(object):

    __metaclass__ = abc.ABCMeta
    
    @abstractclassmethod
    def test(cls):
        """Test method"""
        return cls()


class ClassRegistered(ClassBase):
    
    @classmethod
    def test(cls):
        return True

        
def test_abstractclassmethod_base():
    
    with pytest.raises(TypeError):
        test = ClassBase.test()
        
def test_abstractclassmethod_register():
        
    assert ClassRegistered.test()


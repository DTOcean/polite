# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 15:24:33 2016

@author: 108630
"""

import os

from polite.paths import (Directory, 
                          UserDataDirectory,
                          SiteDataDirectory,
                          object_path,
                          object_dir,
                          class_path,
                          class_dir)
                          
class Test(object):
    
    def test(self):
        
        return True
                          
def test_makedir(tmpdir):
    
    # Make a local directory
    locd = tmpdir.mkdir("test")
    locp = locd.join("test")
    
    test = Directory(str(locp))
    test.makedir()
    
    assert os.path.isdir(str(locp))

def test_UserDataDirectory():
    
    test = UserDataDirectory("test", "test")
    path = test.get_path()
    
    assert isinstance(path, basestring)
        
def test_SiteDataDirectory():
    
    test = SiteDataDirectory("test", "test")
    path = test.get_path()
    
    assert isinstance(path, basestring)
    
def test_object_path():
    
    test = Test()
    
    test_path = object_path(test)
    
    assert os.path.normcase(test_path) == os.path.normcase(__file__)
    
def test_object_dir():
    
    test = Test()
    
    test_path = object_dir(test)
    this_dir = os.path.dirname(__file__)
    
    assert os.path.normcase(test_path) == os.path.normcase(this_dir)
    
def test_class_path():
        
    test_path = class_path(Test)
    
    assert os.path.normcase(test_path) == os.path.normcase(__file__)
    
def test_class_dir():
        
    test_path = class_dir(Test)
    this_dir = os.path.dirname(__file__)
    
    assert os.path.normcase(test_path) == os.path.normcase(this_dir)



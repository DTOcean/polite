# -*- coding: utf-8 -*-

#pylint: disable=missing-docstring,wrong-import-order

import os
import sys
from distutils.cmd import Command

import yaml
from setuptools import setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]
    
    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []
    
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True
    
    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


class CleanPyc(Command):
    
    description = 'clean *.pyc'
    user_options = []
    exclude_list = ['.egg', '.git', '.idea', '__pycache__']
     
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        print "start cleanup pyc files."
        for pyc_path in self.pickup_pyc():
            print "remove pyc: {0}".format(pyc_path)
            os.remove(pyc_path)
        print "the end."
    
    def pickup_pyc(self):
        for root, _, files in os.walk(os.getcwd()):
            for fname in files:
                if self.is_exclude(root):
                    continue
                if not self.is_pyc(fname):
                    continue
                yield os.path.join(root, fname)
    
    @classmethod
    def is_exclude(cls, path):
        for item in CleanPyc.exclude_list:
            if path.find(item) != -1:
                return True
        return False
    
    @classmethod
    def is_pyc(cls, path):
        return path.endswith('.pyc')


def read_yaml(rel_path):
    with open(rel_path, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded


def get_appveyor_version():
    
    data = read_yaml("appveyor.yml")
    
    if "version" not in data:
        raise RuntimeError("Unable to find version string.")
    
    appveyor_version = data["version"]
    last_dot_idx = appveyor_version.rindex(".")
    
    return appveyor_version[:last_dot_idx]


setup(name='polite',
      version=get_appveyor_version(),
      description='Easy functions for paths, logging and configuration files',
      author='Mathew Toppper',
      author_email='mathew.topper@dataonlygreater.com',
      license="MIT",
      packages=['polite'],
      package_data={'polite': ['config/*.yaml']},
      install_requires=[
          'configobj',
          'pyyaml',
          'setuptools'
      ],
      tests_require=['pytest'],
      cmdclass={'test': PyTest,
                'cleanpyc': CleanPyc,
                },
      )

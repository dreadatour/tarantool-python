#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import unittest
import setuptools


from glob import glob

class test(setuptools.Command):
    user_options = []
    description = 'Run unit tests'

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        '''
        Find all tests in test/tarantool/ and run them
        '''
        #root = os.path.dirname(os.path.dirname(__file__))
        #sys.path.insert(0, root)
              
        tests = unittest.defaultTestLoader.discover('tests')
        test_runner = unittest.TextTestRunner(verbosity = 2)
        test_runner.run(tests)

#!/opt/apps/intel13/python/2.7.9/bin/python

## hello world 
# @file test_parse.py
# @author W. Cyrus Proctor
# @date 2015-04-15
# @note TACC
# @copyright License
#
#
# Detailed description

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# System Modules
#import argparse
import unittest

#------------------------------------------------------------------------------

# Local Modules
import config
from parse import Parse

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# Unit Testing #---------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

##
#
#
class TestParse(unittest.TestCase):


  def test_no_cml_args(self):
    cml_args = []
    obj = Parse(test_cml_args=cml_args)
    self.assertTrue(obj)
  def test_debug(self):
    cml_args = ["--debug"]
    obj = Parse(test_cml_args=cml_args)
    self.assertEqual(obj.idev_debug, True)
    config.debug = False # Reset global variable
  def test_valid_num_tasks(self):
    num_task_list = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,\
                     100,500,1000,10000,100000,1000000]
    for task_num in num_task_list:
      cml_args = ["-n",str(task_num)]
      obj = Parse(test_cml_args=cml_args)
      self.assertEqual(obj.idev_tasks,int(task_num))
#  def test_invalid_num_tasks(self):
#    num_task_list = [-1,-2]
#    for task_num in num_task_list:
#      cml_args = ["-n",str(task_num)]
#      self.assertRaises(argparse.ArgumentTypeError,
#                        Parse(test_cml_args=cml_args))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
  runner = unittest.TextTestRunner(verbosity=2)
  itersuite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
  runner.run(itersuite)
  #unittest.main()
  #parse()











#import nose.tools as nt
#
#
#class TestA(object):
#  @classmethod
#  def setup_class(klass):
#    """This method is run once for each class before any tests are run"""
#
#  @classmethod
#  def teardown_class(klass):
#    """This method is run once for each class _after_ all tests are run"""
#
#  def setUp(self):
#    """This method is run once before _each_ test method is executed"""
#
#  def teardown(self):
#    """This method is run once after _each_ test method is executed"""
#
#  def test_init(self):
#    a = A()
#    nt.assert_equal(a.value, "Some Value")
#    nt.assert_not_equal(a.value, "Incorrect Value")
#
#  def test_return_true(self):
#   a = A()
#   nt.assert_equal(a.return_true(), True)
#   nt.assert_not_equal(a.return_true(), False)
#
#  def test_raise_exc(self):
#    a = A()
#    nt.assert_raises(KeyError, a.raise_exc, "A value")
#
##  @raises(KeyError)
##  def test_raise_exc_with_decorator(self):
##    a = A()
##    a.raise_exc("A message")

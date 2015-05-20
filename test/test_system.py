#!/opt/apps/intel13/python/2.7.9/bin/python

## hello world 
# @file test_system.py
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
import unittest

#------------------------------------------------------------------------------

# Local Modules
import idev_exceptions
import system

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
class TestSystem(unittest.TestCase):

  ## Empty initializer should raise TypeError
  def test_empty(self):
    with self.assertRaises(TypeError):
      obj = system.System()
  
  ## Initializer with too many arguments should raise TypeError
  def test_too_many_args(self):
    with self.assertRaises(TypeError):
      obj = system.System("foo", "bar")

  ## Unknown sys_name should raise idev_exceptions.ClassAttributeError 
  def test_wrong_sys_name(self):
    with self.assertRaises(idev_exceptions.ClassAttributeError):
      obj = system.System(name="wrong")


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
  runner = unittest.TextTestRunner(verbosity=2)
  itersuite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
  runner.run(itersuite)

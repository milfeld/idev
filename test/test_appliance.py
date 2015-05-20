#!/opt/apps/intel13/python/2.7.9/bin/python

## hello world 
# @file test_appliance.py
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
import appliance

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
class TestAppliance(unittest.TestCase):

  ## Empty initializer should raise TypeError
  def test_empty(self):
    with self.assertRaises(TypeError):
      obj = appliance.Appliance()
  
  ## Initializer with too many arguments should raise TypeError
  def test_too_many_args(self):
    with self.assertRaises(TypeError):
      obj = appliance.Appliance("foo", "bar", "baz")

  ## Unknown sys_name should raise idev_exceptions.ClassAttributeError 
  def test_wrong_sys_name(self):
    with self.assertRaises(idev_exceptions.ClassAttributeError):
      obj = appliance.Appliance(sys_name="wrong",
                                app_name="compute")
  
  ## Unknown app_name should raise idev_exceptions.ClassAttributeError 
  def test_wrong_app_name(self):
    with self.assertRaises(idev_exceptions.ClassAttributeError):
      obj = appliance.Appliance(sys_name="stampede",
                                app_name="wrong")

  ## Confirm different cases are allowed for initializer names
  def test_stampede_compute(self):
    obj = appliance.Appliance(sys_name="StAmPeDe",
                              app_name="cOmPuTe")
    self.assertIsInstance(obj,appliance.Appliance)

  ## Confirm Stampede Compute Appliance Attributes
  def test_stampede_compute(self):
    obj = appliance.Appliance(sys_name="stampede",
                              app_name="compute")
    self.assertIsInstance(obj,appliance.Appliance)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.app_name)
    self.assertIsNotNone(obj.cores_per_node)
    self.assertIsNotNone(obj.cores_per_socket)
    self.assertIsNotNone(obj.num_sockets)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.app_name,         "compute"  )
    self.assertEqual(obj.cores_per_node,   16         )
    self.assertEqual(obj.cores_per_socket, 8          )
    self.assertEqual(obj.num_sockets,      2          )
  
  ## Confirm different cases are allowed for initializer names
  def test_stampede_compute(self):
    obj = appliance.Appliance(sys_name="StAmPeDe",
                              app_name="cOmPuTe")
    self.assertIsInstance(obj,appliance.Appliance)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.app_name)
    self.assertIsNotNone(obj.cores_per_node)
    self.assertIsNotNone(obj.cores_per_socket)
    self.assertIsNotNone(obj.num_sockets)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.app_name,         "compute"  )
    self.assertEqual(obj.cores_per_node,   16         )
    self.assertEqual(obj.cores_per_socket, 8          )
    self.assertEqual(obj.num_sockets,      2          )
  
  ## Confirm Stampede Bigmem Appliance Attributes
  def test_stampede_bigmem(self):
    obj = appliance.Appliance(sys_name="stampede",
                              app_name="bigmem")
    self.assertIsInstance(obj,appliance.Appliance)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.app_name)
    self.assertIsNotNone(obj.cores_per_node)
    self.assertIsNotNone(obj.cores_per_socket)
    self.assertIsNotNone(obj.num_sockets)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.app_name,         "bigmem"   )
    self.assertEqual(obj.cores_per_node,   32         )
    self.assertEqual(obj.cores_per_socket, 8          )
    self.assertEqual(obj.num_sockets,      4          )

  ## Confirm Stampede Vis Appliance Attributes
  def test_stampede_vis(self):
    obj = appliance.Appliance(sys_name="stampede",
                              app_name="vis")
    self.assertIsInstance(obj,appliance.Appliance)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.app_name)
    self.assertIsNotNone(obj.cores_per_node)
    self.assertIsNotNone(obj.cores_per_socket)
    self.assertIsNotNone(obj.num_sockets)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.app_name,         "vis"      )
    self.assertEqual(obj.cores_per_node,   16         )
    self.assertEqual(obj.cores_per_socket, 8          )
    self.assertEqual(obj.num_sockets,      2          )


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
  runner = unittest.TextTestRunner(verbosity=2)
  itersuite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
  runner.run(itersuite)

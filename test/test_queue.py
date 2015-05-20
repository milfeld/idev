#!/opt/apps/intel13/python/2.7.9/bin/python

## hello world 
# @file test_queue.py
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
import queue

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
      obj = queue.Queue()

  ## Initializer with too many arguments should raise TypeError
  def test_too_many_args(self):
    with self.assertRaises(TypeError):
      obj = queue.Queue("foo", "bar", "baz")

  ## Unknown sys_name should raise idev_exceptions.ClassAttributeError 
  def test_wrong_sys_name(self):
    with self.assertRaises(idev_exceptions.ClassAttributeError):
      obj = queue.Queue(sys_name="wrong",
                        queue_name="normal")
  
  ## Unknown queue_name should raise idev_exceptions.ClassAttributeError 
  def test_wrong_app_name(self):
    with self.assertRaises(idev_exceptions.ClassAttributeError):
      obj = queue.Queue(sys_name="stampede",
                        queue_name="wrong")

  ## Confirm different cases are allowed for initializer names
  def test_stampede_compute(self):
    obj = queue.Queue(sys_name="StAmPeDe",
                      queue_name="nOrMaL")
    self.assertIsInstance(obj,queue.Queue)

  ## Confirm Stampede Normal Queue Attributes
  def test_stampede_normal(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="normal")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "normal"   )
    self.assertEqual(obj.max_runtime,      2880       )
    self.assertEqual(obj.max_nodes,        256        )
    self.assertEqual(obj.max_procs,        4096       )
    self.assertEqual(obj.charge_rate,      1          )
  
  ## Confirm Stampede Development Queue Attributes
  def test_stampede_development(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="development")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede"    )
    self.assertEqual(obj.queue_name,       "development" )
    self.assertEqual(obj.max_runtime,      120           )
    self.assertEqual(obj.max_nodes,        16            )
    self.assertEqual(obj.max_procs,        256           )
    self.assertEqual(obj.max_jobs,         1             )
    self.assertEqual(obj.charge_rate,      1             )

  ## Confirm Stampede Largemem Queue Attributes
  def test_stampede_largemem(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="largemem")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "largemem" )
    self.assertEqual(obj.max_runtime,      2880       )
    self.assertEqual(obj.max_nodes,        4          )
    self.assertEqual(obj.max_procs,        128        )
    self.assertEqual(obj.max_jobs,         4          )
    self.assertEqual(obj.charge_rate,      2          )

  ## Confirm Stampede Serial Queue Attributes
  def test_stampede_serial(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="serial")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "serial"   )
    self.assertEqual(obj.max_runtime,      720        )
    self.assertEqual(obj.max_nodes,        1          )
    self.assertEqual(obj.max_procs,        16         )
    self.assertEqual(obj.max_jobs,         8          )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Large Queue Attributes
  def test_stampede_large(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="large")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "large"    )
    self.assertEqual(obj.max_runtime,      1440       )
    self.assertEqual(obj.max_nodes,        1024       )
    self.assertEqual(obj.max_procs,        16384      )
    self.assertEqual(obj.max_jobs,         50         )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Request Queue Attributes
  def test_stampede_request(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="request")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "request"  )
    self.assertEqual(obj.max_runtime,      1440       )
    self.assertEqual(obj.max_nodes,        6416       )
    self.assertEqual(obj.max_procs,        102656     )
    self.assertEqual(obj.max_jobs,         50         )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Normal-mic Queue Attributes
  def test_stampede_normal_mic(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="normal-mic")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede"   )
    self.assertEqual(obj.queue_name,       "normal-mic" )
    self.assertEqual(obj.max_runtime,      2880         )
    self.assertEqual(obj.max_nodes,        256          )
    self.assertEqual(obj.max_procs,        4096         )
    self.assertEqual(obj.max_jobs,         50           )
    self.assertEqual(obj.charge_rate,      1            )

  ## Confirm Stampede Normal-2mic Queue Attributes
  def test_stampede_normal_2mic(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="normal-2mic")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede"    )
    self.assertEqual(obj.queue_name,       "normal-2mic" )
    self.assertEqual(obj.max_runtime,      1440          )
    self.assertEqual(obj.max_nodes,        128           )
    self.assertEqual(obj.max_procs,        2048          )
    self.assertEqual(obj.max_jobs,         50            )
    self.assertEqual(obj.charge_rate,      1             )

  ## Confirm Stampede Gpu Queue Attributes
  def test_stampede_gpu(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="gpu")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "gpu"      )
    self.assertEqual(obj.max_runtime,      1440       )
    self.assertEqual(obj.max_nodes,        32         )
    self.assertEqual(obj.max_procs,        512        )
    self.assertEqual(obj.max_jobs,         50         )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Gpudev Queue Attributes
  def test_stampede_gpudev(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="gpudev")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "gpudev"   )
    self.assertEqual(obj.max_runtime,      240        )
    self.assertEqual(obj.max_nodes,        4          )
    self.assertEqual(obj.max_procs,        64         )
    self.assertEqual(obj.max_jobs,         5          )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Vis Queue Attributes
  def test_stampede_vis(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="vis")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "vis"      )
    self.assertEqual(obj.max_runtime,      480        )
    self.assertEqual(obj.max_nodes,        32         )
    self.assertEqual(obj.max_procs,        512        )
    self.assertEqual(obj.max_jobs,         50         )
    self.assertEqual(obj.charge_rate,      1          )

  ## Confirm Stampede Gpudev Queue Attributes
  def test_stampede_gpudev(self):
    obj = queue.Queue(sys_name="stampede",
                      queue_name="gpudev")
    self.assertIsInstance(obj,queue.Queue)
    self.assertIsNotNone(obj.sys_name)
    self.assertIsNotNone(obj.queue_name)
    self.assertIsNotNone(obj.max_runtime)
    self.assertIsNotNone(obj.max_nodes)
    self.assertIsNotNone(obj.max_procs)
    self.assertIsNotNone(obj.max_jobs)
    self.assertIsNotNone(obj.charge_rate)
    self.assertEqual(obj.sys_name,         "stampede" )
    self.assertEqual(obj.queue_name,       "gpudev"   )
    self.assertEqual(obj.max_runtime,      240        )
    self.assertEqual(obj.max_nodes,        4          )
    self.assertEqual(obj.max_procs,        64         )
    self.assertEqual(obj.max_jobs,         5          )
    self.assertEqual(obj.charge_rate,      1          )







#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
  runner = unittest.TextTestRunner(verbosity=2)
  itersuite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
  runner.run(itersuite)

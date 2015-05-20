#!/opt/apps/intel13/python/2.7.9/bin/python

## Queue Class 
# @file queue.py
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

#------------------------------------------------------------------------------

# Local Modules
import idev_exceptions

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

## Queue Class
#
# Hold specific queue details which are system dependent.
# A queue must be defined in the Queue._queue_options dictionary
# with an appropriate initialization routine.
# @todo Add an attribute to store what type of Appliance is used in a specfic Queue instance.
#
class Queue(object):

  ## Convert hours to minutes
  #
  # @param hour 
  # @returns hour converted to minutes
  def _hour2min(self,hour):
    return hour * 60

  ## Stampede normal queue specific attributes
  def _init_stampede_normal(self):
    self.max_runtime = self._hour2min(48)
    self.max_nodes   = 256
    self.max_procs   = 4096
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede development queue specific attributes
  def _init_stampede_development(self):
    self.max_runtime = self._hour2min(2)
    self.max_nodes   = 16
    self.max_procs   = 256
    self.max_jobs    = 1
    self.charge_rate = 1

  ## Stampede largemem queue specific attributes
  def _init_stampede_largemem(self):
    self.max_runtime = self._hour2min(48)
    self.max_nodes   = 4
    self.max_procs   = 128
    self.max_jobs    = 4
    self.charge_rate = 2

  ## Stampede serial queue specific attributes
  def _init_stampede_serial(self):
    self.max_runtime = self._hour2min(12)
    self.max_nodes   = 1
    self.max_procs   = 16
    self.max_jobs    = 8
    self.charge_rate = 1

  ## Stampede large queue specific attributes
  def _init_stampede_large(self):
    self.max_runtime = self._hour2min(24)
    self.max_nodes   = 1024
    self.max_procs   = 16384
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede request queue specific attributes
  def _init_stampede_request(self):
    self.max_runtime = self._hour2min(24)
    self.max_nodes   = 6416
    self.max_procs   = 102656
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede normal-mic queue specific attributes
  def _init_stampede_normal_mic(self):
    self.max_runtime = self._hour2min(48)
    self.max_nodes   = 256
    self.max_procs   = 4096
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede normal-2mic queue specific attributes
  def _init_stampede_normal_2mic(self):
    self.max_runtime = self._hour2min(24)
    self.max_nodes   = 128
    self.max_procs   = 2048
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede gpu queue specific attributes
  def _init_stampede_gpu(self):
    self.max_runtime = self._hour2min(24)
    self.max_nodes   = 32
    self.max_procs   = 512
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede gpudev queue specific attributes
  def _init_stampede_gpudev(self):
    self.max_runtime = self._hour2min(4)
    self.max_nodes   = 4
    self.max_procs   = 64
    self.max_jobs    = 5
    self.charge_rate = 1

  ## Stampede vis queue specific attributes
  def _init_stampede_vis(self):
    self.max_runtime = self._hour2min(8)
    self.max_nodes   = 32
    self.max_procs   = 512
    self.max_jobs    = 50
    self.charge_rate = 1

  ## Stampede visdev queue specific attributes
  def _init_stampede_visdev(self):
    self.max_runtime = self._hour2min(4)
    self.max_nodes   = 4
    self.max_procs   = 64
    self.max_jobs    = 5
    self.charge_rate = 1

  ## Class attribute of defined (system, queue) tuple pairs
  # Tuple name string is associated with proper instance method to call
  _queue_options = { ("stampede", "normal"     ) : _init_stampede_normal,
                     ("stampede", "development") : _init_stampede_development,
                     ("stampede", "largemem"   ) : _init_stampede_largemem,
                     ("stampede", "serial"     ) : _init_stampede_serial,
                     ("stampede", "large"      ) : _init_stampede_large,
                     ("stampede", "request"    ) : _init_stampede_request,
                     ("stampede", "normal-mic" ) : _init_stampede_normal_mic,
                     ("stampede", "normal-2mic") : _init_stampede_normal_2mic,
                     ("stampede", "gpu"        ) : _init_stampede_gpu,
                     ("stampede", "gpudev"     ) : _init_stampede_gpudev,
                     ("stampede", "vis"        ) : _init_stampede_vis,
                     ("stampede", "visdev"     ) : _init_stampede_visdev,
  } 

  ## Queue Initializer
  #
  # Given the name of the system and the name of the queue, assuming
  # that the tuple pair (system_name, queue_name) is defined in
  # Queue._queue_options, queue specific attributues will be
  # populated.
  # 
  # @param sys_name Name of the compute system
  # @param queue_name Name of the queue to be initialized
  # @returns An initialized instance of a Queue class object
  #
  def __init__(self,
               sys_name,
               queue_name):
    self.sys_name    = sys_name.lower()
    self.queue_name  = queue_name.lower()
    # Create tuple key
    self.key         = (self.sys_name, self.queue_name)
    # Call appropriate initializer method based on key
    try:
      Queue._queue_options[self.key](self)
    except KeyError:
      message = "Invalid initialization tuple key (sys_name, queue_name)"
      raise idev_exceptions.ClassAttributeError(message, self._queue_options.keys())

  ## Display Queue Instance Information
  #
  # Print out the name and subsequent queue attributes associated
  # with the particular instance.
  #
  def display(self):
    print("Queue Name:           {}".format(self.queue_name))
    print("Max Run Time (mins):  {}".format(self.max_runtime))
    print("Max Node Count:       {}".format(self.max_nodes))
    print("Max Process Count:    {}".format(self.max_procs))
    print("Max Jobs in Queue:    {}".format(self.max_jobs))
    print("Queue SU Charge Rate: {}".format(self.charge_rate))









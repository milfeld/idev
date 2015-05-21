#!/opt/apps/intel13/python/2.7.9/bin/python

## System Class 
# @file system.py
# @author W. Cyrus Proctor
# @date 2015-05-08
# @note TACC
# @copyright License
#
#
# Detailed description

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# System Modules
import copy

#------------------------------------------------------------------------------

# Local Modules
import idev_exceptions
import appliance
import queue

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

## System Class
#
# Holds specific system information including lists of all
# appliances and queues, along with their associated attributes
# collected in dictionaries populated with Appliance and Queue 
# class instances. Designed for easy reference of system information.
#
# A system must be defined in the System._sys_options dictionary along
# with an appropriate initization routine.
#
class System(object):

  ## Stampede specific appliance and queue names
  def _init_stampede(self):
    self.app_name_list   = ["compute",
                            "bigmem",
                            "vis"]
  
    self.queue_name_list = ["normal",
                            "development",
                            "largemem",
                            "serial",
                            "large",
                            "request",
                            "normal-mic",
                            "normal-2mic",
                            "gpu",
                            "gpudev",
                            "vis",
                            "visdev"]

  ## Lonestar specific appliance and queue names
  def _init_lonestar(self):
    pass

  ## Maverick specific appliance and queue names
  def _init_maverick(self):
    pass

  ## Wrangler specific appliance and queue names
  def _init_wrangler(self):
    pass
 
  ## Class attribute of defined systems
  # Name string is associated with proper instance method to call
  _sys_options = { "stampede" : _init_stampede,
                   "lonestar" : _init_lonestar,
                   "maverick" : _init_maverick,
                   "wrangler" : _init_wrangler,
  }
  
  ## System Initializer
  #
  # Given the name of the system and assuming it is defined in 
  # System._sys_options, two lists will be populated: app_name_list
  # and queue_name_list. For each name in these lists, Appliance
  # and Queue class instances will be initialized with the appropriate
  # information.
  #
  # @param name System name as defined in System._sys_options
  # @returns An initialized instance of a System class object
  #
  def __init__(self,
               name):
    # Convert to all lowercase
    self.name = name.lower()
    # Call the appropriate init function based on system name
    try:
      System._sys_options[self.name](self)
    except KeyError:
      message = "Invalid initialization key (system name)"
      raise idev_exceptions.ClassAttributeError(message, self._sys_options.keys())
   
    # For each appliance, populate a new Appliance instance in a dict
    self.app = dict() 
    for app_name in self.app_name_list:
      self.app[app_name] = appliance.Appliance(self.name,app_name)
    
    # For each queue, populate a new Queue instance in a dict
    self.queue = dict()
    for queue_name in self.queue_name_list:
      self.queue[queue_name] = queue.Queue(self.name, queue_name)


  ## Display System Instance Information
  #
  # Print out the name and each subsequent appliance and queue
  # associated with the system instance.
  #
  def display(self):
    print ("System Name: {}".format(self.name))
    for app_name in self.app_name_list:
      print "="*50
      self.app[app_name].display()
    for queue_name in self.queue_name_list:
      print "="*50
      self.queue[queue_name].display() 
    


#a = System(name="Stampede")
#a.display()
#a.queue["normal"].display()

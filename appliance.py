#!/opt/apps/intel13/python/2.7.9/bin/python

## Appliance Module 
# @file appliance.py
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

## Appliance Class
#
# Holds specific appliance details which are system dependent.
#
# An appliance must be defined in the Appliance._app_options dictionary
# with an appropriate initialization routine.
#
class Appliance(object):

  ## Stampede compute appliance specific attributes
  def _init_stampede_compute(self):
    self.app_name         = "compute"
    self.cores_per_node   = 16
    self.cores_per_socket = 8
    self.num_sockets      = 2

  ## Stampede bigmem appliance specific attributes
  def _init_stampede_bigmem(self):
    self.app_name         = "bigmem"
    self.cores_per_node   = 32
    self.cores_per_socket = 8
    self.num_sockets      = 4

  ## Stampede vis appliance specific attributes
  def _init_stampede_vis(self):
    self.app_name         = "vis"
    self.cores_per_node   = 16
    self.cores_per_socket = 8
    self.num_sockets      = 2
  
  ## Class attribute of defined (system, appliance) tuple pairs
  # Tuple name string is associated with proper instance method to call
  _app_options = { ("stampede", "compute") : _init_stampede_compute,
                   ("stampede", "bigmem" ) : _init_stampede_bigmem,
                   ("stampede", "vis"    ) : _init_stampede_vis,
  }
    
  ## Appliance Initializer
  #
  # Given the name of the system and the name of the appliance, assuming
  # that the tuple pair (system_name, appliance_name) is defined in 
  # Appliance._app_options, appliance specific attributes will be
  # populated.
  #
  # @param sys_name Name of the compute system
  # @param app_name Name of the appliance to be initialized
  # @returns An initialized instance of an Appliance class object
  #
  def __init__(self,
               sys_name,
               app_name):
    self.sys_name = sys_name.lower()
    self.app_name = app_name.lower()
    # Create tuple key
    self.key = (self.sys_name, self.app_name)
    # Call appropriate initializer method based on key
    try:
      Appliance._app_options[self.key](self)
    except KeyError:
      message = "Invalid initialization tuple key (sys_name, app_name)"
      raise idev_exceptions.ClassAttributeError(message, self._app_options.keys())

  ## Display Appliance Instance Information
  #
  # Print out the name and subsequent appliance attributes associated
  # with this particular instance.
  #
  def display(self):
    print("Appliance Name:             {}".format(self.app_name))
    print("Number of Cores per Node:   {}".format(self.cores_per_node))
    print("Number of Cores per Socket: {}".format(self.cores_per_socket))
    print("Number of Sockets per Node: {}".format(self.num_sockets))
















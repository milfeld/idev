#!/opt/apps/intel13/python/2.7.9/bin/python

## Idev custom exceptions module 
# @file idev_exceptions.py
# @author W. Cyrus Proctor
# @date 2015-05-20
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


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

## custom exception
#
#
class IdevArgumentError(Exception):
   ## exception constructor
   def __init__(self, message, errors=None):

    # Call the base class constructor with the parameters it needs
    super(IdevArgumentError, self).__init__(message)

    # Now for your custom code...
    self.errors = errors

## custom exception
#
#
class ClassAttributeError(Exception):
  
  ## ClassAttributeError Initializer
  #
  # Take a message and a list of valid keys to display
  #
  # @param message Error message to display
  # @param keys a list of keys to display as valid calling options
  #
  def __init__(self, message, keys=None):

    # Add custom text to print out available key options
    message += "\n\nValid keys include:\n"
    for key in keys:
      message += str(key) + "\n"

    # Call the base class constructor with the parameters it needs
    super(ClassAttributeError, self).__init__(message)

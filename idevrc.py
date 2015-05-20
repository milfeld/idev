#!/opt/apps/intel13/python/2.7.9/bin/python

## Idevrc Class 
# @file idevrc.py
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
import Queue

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


## My idevrc data class
#
# Detailed description
# 
class Idevrc(Queue):
  ## Idevrc constructor
  #
  # @todo Hold idevrc default information
  #
  def __init__(self                      , 
               project             = None,
               min_time            = None, 
               queue               = None):
    self.project  = project
    self.min_time = min_time
    self.hms_time = min2hms(min_time)
    self.queue    = queue or super(Idevrc, self).__init__()



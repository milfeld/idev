#!/opt/apps/intel13/python/2.7.9/bin/python
# W. Cyrus Proctor
# 2015-04-15
# TACC
# License

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# System Modules
import argparse
import datetime

#------------------------------------------------------------------------------

# Local Modules
import config
import iterable as it
from decorators import timing, echo


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

## Convert time in (int) minutes to time in "hh:mm:ss" (str) format
#
#  Given integer min_time, return a formatted string in 
#  hours, minutes, and seconds separated by colons.
#
#  @param min_time integer containing time, in minutes to convert
#
#  Returns a string hms_time formatted as "hh:mm:ss"
#
def min2hms(min_time):
  """Convert time in (int) minutes to time in hh:mm:ss (str) format"""
  s = 0
  h, m = divmod(min_time, 60)
  hms_time = "%02d:%02d:%02d" % (h, m, s)
  return hms_time

#------------------------------------------------------------------------------

## Define all known run-time command-line arguments
#
# Given an argparse.ArgumentParser instance, add required, optional and mutually
# exclusive command-line arguments and return.
#
# @param parser is an intialized instance of argparse.ArgumentParser class
#
# Returns the instance with the arguments added.
@timing
@echo
def add_arguments(parser):
  """ testing add_arguments"""
  
  # Will parse out of .idevrc
  idevrc_project    = "A-ccsc"                 # TACC internal
  idevrc_min_time   = 30                       # (minutes)
  idevrc_hms_time   = min2hms(idevrc_min_time) # hh:mm:ss
  idevrc_queue      = "development"            # TACC internal

  # Defaults
  default_account   = it.ensure_iterable_variable(idevrc_project)
  default_min_time  = it.ensure_iterable_variable(idevrc_min_time)
  default_hms_time  = it.ensure_iterable_variable(idevrc_hms_time)
  default_queue     = it.ensure_iterable_variable(idevrc_queue)
  default_num_tasks = it.ensure_iterable_variable(16) # System dependent
  default_num_nodes = it.ensure_iterable_variable(1)
  
  parser.add_argument('-v',
                      '--version',
                      action   = 'version', 
                      version  = '%(prog)s {}'.format(config.version))
  parser.add_argument('-A', 
                      nargs    = 1, 
                      type     = str, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_project', 
                      default  = default_account, 
                      metavar  = ('project_name'), 
                      help     = "Project allocation name for SU accounting")
  # -N may not be present without -n; leave default as None for postprocessing
  parser.add_argument('-n', 
                      nargs    = 1, 
                      type     = int, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_tasks', 
                      default  = None, 
                      metavar  = ('num_tasks'), 
                      help     = "total number of MPI tasks")
  # -N may not be present without -n; leave default as None for postprocessing
  parser.add_argument('-N', 
                      nargs    = 1, 
                      type     = int, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_nodes', 
                      default  = None, 
                      metavar  = ('num_nodes'), 
                      help     = "total number of compute nodes")
  # -p and -q are mutually exclusive
  queue_group = parser.add_mutually_exclusive_group()
  queue_group.add_argument('-p', 
                           nargs    = 1, 
                           type     = str, 
                           required = False, 
                           action   = 'store', 
                           dest     = 'idev_queue', 
                           default  = default_queue, 
                           metavar  = ('queue_name'), 
                           help     = "set which named queue to run the session in")
  queue_group.add_argument('-q', 
                           nargs    = 1, 
                           type     = str, 
                           required = False, 
                           action   = 'store', 
                           dest     = 'idev_queue', 
                           default  = default_queue, 
                           metavar  = ('queue_name'), 
                           help     = "set which named queue to run the session in")

  # -t and -m are mutually exclusive
  time_group = parser.add_mutually_exclusive_group()
  time_group.add_argument('-m', 
                          nargs    = 1, 
                          type     = int, 
                          required = False, 
                          action   = 'store', 
                          dest     = 'idev_min_time', 
                          default  = default_min_time, 
                          metavar  = ('minutes'), 
                          help     = "idev session length in minutes")
  time_group.add_argument('-t', 
                          nargs    = 1, 
                          type     = str, 
                          required = False, 
                          action   = 'store', 
                          dest     = 'idev_hms_time', 
                          default  = default_hms_time, 
                          metavar  = ('hms_time'), 
                          help     = "idev session length in hh:mm:ss")
  


  return parser
#------------------------------------------------------------------------------

class Appliance:
  """ Test Appliance"""
  def __init__(self, cores_per_node):
    """ Test Appliance init"""
    self.cores_per_node = cores_per_node
  # TODO: Hold appliance-specific information -- core counts, etc.
#------------------------------------------------------------------------------

class Idevrc(Appliance):
  """Test Idevrc"""
  def __init__(self, project, min_time, queue):
    """ Test Idevrc init"""
    self.project  = project
    self.min_time = min_time
    self.hms_time = min2hms(min_time)
    self.queue    = queue
  # TODO: Hold idevrc default information


#------------------------------------------------------------------------------

@timing
@echo
def parse():
  """ Test parse"""

  # idev introductory help message
  idev_prologue = \
                  """
                  idev creates an interactive session on a compute node
                  for executing serial, openmp-parallel, or mpi-parallel
                  code as you would in a batch job.\
                  Supported systems: Stampede
                  """
  # idev ending help message
  idev_epilog = """TACC4LIFE"""
  # Create instance of argument parser
  parser = argparse.ArgumentParser(prog=config.name,
                                   description=idev_prologue,
                                   epilog=idev_epilog)
  # Add command-line arguments to parse
  parser = add_arguments(parser)
  # Parse all known args and bundle the rest into extra
  cl_args, cl_extra_args = parser.parse_known_args()
 
  # TODO: Set -N and and -n correctly if not specified

  # -N is set; -n is not set
  if cl_args.idev_nodes is not None and cl_args.idev_tasks is None:
    # cl_args.idev_tasks = 
    print "-N"

  # -n is set; -N is not set
  elif cl_args.idev_tasks is not None and cl_args.idev_nodes is None:
    print "-n"

  # Neither -N or -n are set
  elif cl_args.idev_tasks is None and cl_args.idev_nodes is None:
    print "neither"

  # Both -N and -n are set
  else:
    print "BOTH"
   


  if config.debug:
    #import __main__
    print("\nSTART TACC DEBUG {}".format(__file__))
    print("Recognized Command-line Arguments:   {}".format(cl_args))
    print("Unrecognized Command-line Arguments: {}".format(cl_extra_args))
    print("END TACC DEBUG {}\n".format(__file__))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
    parse()


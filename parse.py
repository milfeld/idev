#!/opt/apps/intel13/python/2.7.9/bin/python
# W. Cyrus Proctor
# 2015-04-15
# TACC
# License


# System Modules
import argparse

# Local Modules
import config
import iterable as it
from decorators import timing, echo






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
  
  # Will parse out of .idevrc
  idevrc_project       = "A-ccsc"       # TACC internal
  idevrc_time          = 30             # (minutes)
  idevrc_queue         = "development"  # TACC internal

  # Defaults
  default_account      = it.ensure_iterable_variable(idevrc_project)
  default_time_in_mins = it.ensure_iterable_variable(idevrc_time)
  default_queue        = it.ensure_iterable_variable(idevrc_queue)
  default_num_tasks    = it.ensure_iterable_variable(16) # System dependent
  default_num_nodes    = it.ensure_iterable_variable(1)
  
  parser.add_argument('-A', 
                      nargs    = 1, 
                      type     = str, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_project', 
                      default  = default_account, 
                      metavar  = ('account'), 
                      help     = "project account name")
  parser.add_argument('-m', 
                      nargs    = 1, 
                      type     = int, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_time', 
                      default  = default_time_in_mins, 
                      metavar  = ('minutes'), 
                      help     = "idev session length in minutes")
  parser.add_argument('-n', 
                      nargs    = 1, 
                      type     = int, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_tasks', 
                      default  = default_num_tasks, 
                      metavar  = ('total_tasks'), 
                      help     = "total number of MPI tasks")
  parser.add_argument('-p', 
                      nargs    = 1, 
                      type     = str, 
                      required = False, 
                      action   = 'store', 
                      dest     = 'idev_queue', 
                      default  = default_queue, 
                      metavar  = ('queue_name'), 
                      help     = "set which named queue to run the session in")

  # TODO: -t and -m should be mutually exclusive
  # TODO: -N may not be present without -n
  # TODO: -v version option

  return parser

@timing
@echo
def parse():

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
  parser = argparse.ArgumentParser(description=idev_prologue,
                                   epilog=idev_epilog)
  # Add command-line arguments to parse
  parser = add_arguments(parser)
  # Parse all known args and bundle the rest into extra
  cl_args, cl_extra_args = parser.parse_known_args()

  if config.debug:
    #import __main__
    print("\nSTART TACC DEBUG {}".format(__file__))
    print("Recognized Command-line Arguments:   {}".format(cl_args))
    print("Unrecognized Command-line Arguments: {}".format(cl_extra_args))
    print("END TACC DEBUG {}\n".format(__file__))



if __name__ == "__main__":
    parse()


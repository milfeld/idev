#!/opt/apps/intel13/python/2.7.9/bin/python

## hello world 
# @file parse.py
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
import argparse
import datetime
import unittest

#------------------------------------------------------------------------------

# Local Modules
import config
import iterable as it
from decorators import timing, echo


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

## my parse class
#
# @param test_cml_args for unit testing Parse class
#
class Parse():

  def __init__(self, 
               test_cml_args=None):
    # Initialize parser with prologue and epilogue 
    self.init_parser()
    # Add command-line argument definitions to parse
    self.add_arguments()
    # Parse command-line arguments
    self.parse(test_cml_args)
  
  #----------------------------------------------------------------------------

  ## Convert time in (int) minutes to time in "hh:mm:ss" (str) format
  #
  #  Given integer min_time, return a formatted string in 
  #  hours, minutes, and seconds separated by colons.
  #
  #  @param min_time integer containing time, in minutes to convert
  #
  #  Returns a string hms_time formatted as "hh:mm:ss"
  #
  def min2hms(self, 
              min_time):
    s = 0
    h, m = divmod(min_time, 60)
    hms_time = "%02d:%02d:%02d" % (h, m, s)
    return hms_time
  
  #----------------------------------------------------------------------------
  
  ## Define all known run-time command-line arguments
  #
  # Given an argparse.ArgumentParser instance, add required, optional and 
  # mutually exclusive command-line arguments and return.
  #
  # @param parser is an intialized instance of argparse.ArgumentParser class
  #
  # Returns the instance with the arguments added.
  @timing
  @echo
  def add_arguments(self):
    
    # Will parse out of .idevrc
    idevrc_project    = "A-ccsc"                      # TACC internal
    idevrc_min_time   = 30                            # (minutes)
    idevrc_hms_time   = self.min2hms(idevrc_min_time) # hh:mm:ss
    idevrc_queue      = "development"                 # TACC internal
  
    # Defaults
    default_debug_mode = False
    default_account    = idevrc_project
    default_min_time   = idevrc_min_time
    default_hms_time   = idevrc_hms_time
    default_queue      = idevrc_queue
    default_num_tasks  = 16 # System dependent
    default_num_nodes  = 1
    
    self.parser.add_argument('--debug',
                             required = False,
                             action   = 'store_true',
                             dest     = 'idev_debug',
                             default  = default_debug_mode,
                             help     = "enable debug mode")
    self.parser.add_argument('--version',
                             action   = 'version', 
                             version  = '%(prog)s {}'.format(config.version))
    self.parser.add_argument('-A', 
                             nargs    = 1, 
                             type     = str, 
                             required = False, 
                             action   = 'store', 
                             dest     = 'idev_project', 
                             default  = default_account, 
                             metavar  = ('project_name'), 
                             help     = "project allocation name for\
                                         SU accounting")
    # -N may not be present without -n; 
    # Leave default as None for postprocessing
    self.parser.add_argument('-n', 
                             nargs    = 1, 
                             type     = int, 
                             required = False, 
                             action   = _PositiveIntegerAction, 
                             dest     = 'idev_tasks', 
                             default  = None, 
                             metavar  = ('num_tasks'), 
                             help     = "total number of MPI tasks")
    # -N may not be present without -n; 
    # Leave default as None for postprocessing
    self.parser.add_argument('-N', 
                             nargs    = 1, 
                             type     = int, 
                             required = False, 
                             action   = _PositiveIntegerAction, 
                             dest     = 'idev_nodes', 
                             default  = None, 
                             metavar  = ('num_nodes'), 
                             help     = "total number of compute nodes")
    # -p and -q are mutually exclusive
    queue_group = self.parser.add_mutually_exclusive_group()
    queue_group.add_argument('-p', 
                             nargs    = 1, 
                             type     = str, 
                             required = False, 
                             action   = 'store', 
                             dest     = 'idev_queue', 
                             default  = default_queue, 
                             metavar  = ('queue_name'), 
                             help     = "set which named queue to\
                                         run the session in")
    queue_group.add_argument('-q', 
                             nargs    = 1, 
                             type     = str, 
                             required = False, 
                             action   = 'store', 
                             dest     = 'idev_queue', 
                             default  = default_queue, 
                             metavar  = ('queue_name'), 
                             help     = "set which named queue to\
                                         run the session in")
  
    # -t and -m are mutually exclusive
    time_group = self.parser.add_mutually_exclusive_group()
    time_group.add_argument('-m', 
                            nargs    = 1, 
                            type     = int, 
                            required = False, 
                            action   = _PositiveIntegerAction, 
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
    
  
  
    return self.parser


  #----------------------------------------------------------------------------
  
  ## Parse out command-line options for use with pidev
  #
  # Detailed description
  #
  # @test_cml_args Used to send a list of command-line arguments for unit testing
  #
  # @todo Print TACC system defaults 
  # @todo Print User's idevrc defaults
  # @todo Set -N and and -n correctly if not specified
  #
  @timing
  @echo
  def parse(self, test_cml_args=None):
  
    # Parse all known args and bundle the rest into extra
    cml_args, cml_unknown_args = self.parser.parse_known_args(test_cml_args)
  
    if config.debug:
      #import __main__
      print("\nSTART TACC DEBUG {}".format(__file__))
      print("Recognized Command-line Arguments:   {}".format(cml_args))
      print("Unrecognized Command-line Arguments: {}".format(cml_unknown_args))
      print("END TACC DEBUG {}\n".format(__file__))
    
    self.assign_known_args(cml_args)
 
  #----------------------------------------------------------------------------

  def assign_known_args(self, cml_args):
    self.assign_nodes_and_tasks(cml_args)
    self.assign_debug_mode(cml_args)


  #----------------------------------------------------------------------------
  def assign_debug_mode(self, cml_args):
    if cml_args.idev_debug:
      print("Debug mode activated via command-line. Ignoring config.debug")
      self.idev_debug = cml_args.idev_debug
      config.debug    = cml_args.idev_debug
    
  #----------------------------------------------------------------------------

  def init_parser(self):
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
    self.parser = argparse.ArgumentParser(prog=config.name,
                                     description=idev_prologue,
                                     epilog=idev_epilog)

  #----------------------------------------------------------------------------
  def assign_nodes_and_tasks(self, cml_args):

    if self.check_nodes_only(cml_args):
      err_msg = "-N set to {0}; -n NOT set. -n must be set with option -N."\
                .format(self.idev_nodes)
      raise IdevArgumentError(err_msg)

    if self.check_tasks_only(cml_args):
      self.idev_tasks = it.list_to_int(cml_args.idev_tasks)
      appliance_tasks_per_node = 16 # TODO insert applicance
      self.idev_nodes, remainder = divmod(self.idev_tasks, 
                                          appliance_tasks_per_node)
      if remainder > 0: self.idev_nodes += 1
 
    if self.check_no_nodes_no_tasks(cml_args):
      self.idev_nodes = 1  # TODO insert reservation, idevrc, then sys default
      self.idev_tasks = 16 # TODO insert reservation, idevrc, then sys default

    if self.check_nodes_and_tasks(cml_args):
      self.idev_nodes = it.list_to_int(cml_args.idev_nodes)
      self.idev_tasks = it.list_to_int(cml_args.idev_tasks)

  #----------------------------------------------------------------------------
  ## -N is set; -n is not set
  def check_nodes_only(self, cml_args):
    return cml_args.idev_nodes is not None and cml_args.idev_tasks is None
  
  #----------------------------------------------------------------------------
  ## -n is set; -N is not set
  def check_tasks_only(self, cml_args):
    return cml_args.idev_tasks is not None and cml_args.idev_nodes is None
  
  #----------------------------------------------------------------------------
  ## Neither -N or -n are set
  def check_no_nodes_no_tasks(self, cml_args):
    return cml_args.idev_tasks is None and cml_args.idev_nodes is None
  
  #----------------------------------------------------------------------------
  ## Both -N and -n are set
  def check_nodes_and_tasks(self, cml_args):
    return cml_args.idev_tasks is not None and cml_args.idev_nodes is not None
     

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




#------------------------------------------------------------------------------
## My appliance
#
# Detailed description
class Appliance:
  ## Constructor
  #
  # Detailed description
  # @param app_name
  # @param cores_per_node
  # @param cores_per_socket
  # @param num_sockets
  #
  # @todo Hold appliance-specific information -- core counts, etc.
  def __init__(self                      ,
               app_name            = None,
               cores_per_node      = None,
               cores_per_socket    = None,
               num_sockets         = None):
    self.app_name         = app_name
    self.cores_per_node   = cores_per_node
    self.cores_per_socket = cores_per_socket
    self.num_sockets      = num_sockets

#------------------------------------------------------------------------------

## My Queue
#
#
class Queue(Appliance):
  ## queue constructor
  #
  #
  def __init__(self                      ,
               queue_name          = None,
               appliance           = None):
    self.queue_name = queue_name
    self.appliance = appliance or super(Queue, self).__init__()

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


#------------------------------------------------------------------------------
## Positive Integer Checking
#
# description _SingleLeadingUnderscore for weak "internal use" indicator
#
class _PositiveIntegerAction(argparse.Action):

  ## brief stuff
  # Details
  #
  def __call__(self, parser, namespace, values, option_string=None):
   
    for value in values: 
      if not isinstance(value, int):
        parser.error("{0} must be an integer value > 0; received {1}"\
                     .format(option_string, value))
        raise argparse.ArgumentTypeError("Integer Required")
     
      if value <= 0:
        parser.error("{0} must be an integer value > 0; received {1}"\
                     .format(option_string, value))
        raise argparse.ArgumentTypeError("Positive Integer Required")

    setattr(namespace, self.dest, values)







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
class TestParse(unittest.TestCase):


  def test_no_cml_args(self):
    cml_args = []
    obj = Parse(test_cml_args=cml_args)
    self.assertTrue(obj)
  def test_debug(self):
    cml_args = ["--debug"]
    obj = Parse(test_cml_args=cml_args)
    self.assertEqual(obj.idev_debug, True)
    config.debug = False # Reset global variable
  def test_valid_num_tasks(self):
    num_task_list = [1,2,3,4,5,6,7,8,9,10,20,30,40,50,\
                     100,500,1000,10000,100000,1000000]
    for task_num in num_task_list:
      cml_args = ["-n",str(task_num)]
      obj = Parse(test_cml_args=cml_args)
      self.assertEqual(obj.idev_tasks,int(task_num))
#  def test_invalid_num_tasks(self):
#    num_task_list = [-1,-2]
#    for task_num in num_task_list:
#      cml_args = ["-n",str(task_num)]
#      self.assertRaises(argparse.ArgumentTypeError,
#                        Parse(test_cml_args=cml_args))


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

if __name__ == "__main__":
  runner = unittest.TextTestRunner()
  itersuite = unittest.TestLoader().loadTestsFromTestCase(TestParse)
  runner.run(itersuite)
  #unittest.main()
  #parse()











#import nose.tools as nt
#
#
#class TestA(object):
#  @classmethod
#  def setup_class(klass):
#    """This method is run once for each class before any tests are run"""
#
#  @classmethod
#  def teardown_class(klass):
#    """This method is run once for each class _after_ all tests are run"""
#
#  def setUp(self):
#    """This method is run once before _each_ test method is executed"""
#
#  def teardown(self):
#    """This method is run once after _each_ test method is executed"""
#
#  def test_init(self):
#    a = A()
#    nt.assert_equal(a.value, "Some Value")
#    nt.assert_not_equal(a.value, "Incorrect Value")
#
#  def test_return_true(self):
#   a = A()
#   nt.assert_equal(a.return_true(), True)
#   nt.assert_not_equal(a.return_true(), False)
#
#  def test_raise_exc(self):
#    a = A()
#    nt.assert_raises(KeyError, a.raise_exc, "A value")
#
##  @raises(KeyError)
##  def test_raise_exc_with_decorator(self):
##    a = A()
##    a.raise_exc("A message")

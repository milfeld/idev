#!/opt/apps/intel13/python/2.7.9/bin/python 
# @author W. Cyrus Proctor                          
# @date 2015-04-15                                
# @note TACC                                      
# @copyright License                                   


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# System Modules
import sys
import time
import datetime
import os
import functools

#------------------------------------------------------------------------------

# Local Modules
import config

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

##
#
#
def datetime_to_string():
  t = datetime.datetime.now()

  dtstr = str(t.year) + '-' + \
    str(t.month).zfill(2) + '-' + \
    str(t.day).zfill(2) + '_' + \
    str(t.hour).zfill(2) + '-' + \
    str(t.minute).zfill(2) + '-' + \
    str(t.second).zfill(2)

  return dtstr

#------------------------------------------------------------------------------

##
#
#
def timer(denovo_inst):
  def actualDecorator(test_func):
    @functools.wraps(test_func)
    def wrapper(*args, **kwargs):
      time1 = time.time()
      ret = test_func(*args,**kwargs)
      time2 = time.time()
      if denovo_inst.node() == 0:
        print '%s function took %0.3f s' % (test_func.__name__, (time2-time1))
      return ret 
    return wrapper
  return actualDecorator

#------------------------------------------------------------------------------

##
#
#
def timing(f):
  def wrap(*args,**kwargs):
    time1 = time.time()
    ret = f(*args,**kwargs)
    time2 = time.time()
    if config.timing:
      print '%s function took %0.3f s' % (f.__name__, (time2-time1))
    return ret
  return wrap

#------------------------------------------------------------------------------

##
#
#
def name(item):
  " Return an item's name. "
  return item.__name__

#------------------------------------------------------------------------------

##
#
#    
def format_arg_value(arg_val):
  """ Return a string representing a (name, value) pair.
  
  >>> format_arg_value(('x', (1, 2, 3)))
  'x=(1, 2, 3)'
  """
  arg, val = arg_val
  return "%s=%r" % (arg, val)

#------------------------------------------------------------------------------

##
#
#  
def echo(fn, write=sys.stdout.write):
  """ Echo calls to a function.
  
  Returns a decorated version of the input function which "echoes" calls
  made to it by writing out the function's name and the arguments it was
  called with.
  """
  import functools
  # Unpack function's arg count, arg names, arg defaults
  code        = fn.func_code
  argcount    = code.co_argcount
  argnames    = code.co_varnames[:argcount]
  fn_defaults = fn.func_defaults or list()
  argdefs     = dict(zip(argnames[-len(fn_defaults):], fn_defaults))
  
  ##
  #
  #
  @functools.wraps(fn)
  def wrapped(*v, **k):
    """Collect function arguments by chaining together positional,
    # defaulted, extra positional and keyword arguments.
    """
    positional = map(format_arg_value, zip(argnames, v))
    defaulted  = [format_arg_value((a, argdefs[a]))
                  for a in argnames[len(v):] if a not in k]
    nameless   = map(repr, v[argcount:])
    keyword    = map(format_arg_value, k.items())
    args       = positional + defaulted + nameless + keyword

    if config.debug:
      print("\nSTART TACC DEBUG {}".format(__file__))
      print("{}: ({})".format(name(fn), ", ".join(args)))
      print("END TACC DEBUG {}\n".format(__file__))
    #write("%s(%s)\n" % (name(fn), ", ".join(args)))

    return fn(*v, **k)

  return wrapped

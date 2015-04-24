#!/opt/apps/intel13/python/2.7.9/bin/python
# @author W. Cyrus Proctor
# @date 2015-04-15      
# @note TACC            
# @copyright License         


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

# System modules

#------------------------------------------------------------------------------

# Local modules


#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------


## Try to make a variable iterable
#
# Error checking to see if a variable can be iterable, i.e. to see if it
# can be used as the basis to drive a for loop. If not, then alert
# the user and crash out.
#
# @param variable The variable to be checked to see if one can iterate on it
#
# @verbatim
#                     is variable iterable?
#                              |
#                           -------
#                          |       |
#                         Yes      No
#                          |       |
#                -----------       ---------------
#                |                               |
#         is variable a str?           wrap in square brackets
#                |                               |
#            --------------------         is variable iterable?
#           |                    |               |
#          Yes                   No         --------------------    
#           |                    |         |                    |
#  wrap in square brackets     return     yes                   no
#           |                              |                    |
#         return                         return           unknown error
# @endverbatim
def ensure_iterable_variable(variable):
  if variable == None:
    variable = []
  variable_temp = variable
  try:
    iter(variable)
    if type(variable) == type("dummy"):
      variable_temp = [variable]
  except TypeError:
    variable_temp = [variable]
    try:
      iter(variable_temp)
    except TypeError:
      print "ERROR:",variable,"is not iterable!"
      print "Tried encapsulating in square brackets '[]': Failed"
      exit(-1)

  variable = variable_temp
  return variable


#------------------------------------------------------------------------------


## Check if a variable is iterable.
#
# Error checking to see if a variable is iterable, i.e. to see if it
# can be used as the basis to drive a for loop. If not, then alert
# the user and crash out.
#
# @param variable The variable to be checked to see if one can iterate on it
def iterable_variable_check(variable):
  try:
    iterator = iter(variable)
  except TypeError:
    print "ERROR:",variable,"is not iterable!"
    print "Encapsulate in square brackets '[]'"
    print "or create a range(variable) or xrange(variable)"
    exit(-1)

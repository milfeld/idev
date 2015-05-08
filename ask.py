#!/usr/local/bin/python
#!/opt/apps/intel13/python/2.7.9/bin/python


## User Interaction and Query functions 
# @file ask.py
# @author Kent Milfeld
# @date 2015-05-07
# @note TACC
# @copyright License
#
#
# Detailed description
# Stolen from http://code.activestate.com/recipes/577058/ by Kent Milfeld
# @todo  Write our own version (don't like Capital Letter default: [y/N] )

import sys

#-------------------------------------------------------------------------------

def is_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

# Stolen from http://code.activestate.com/recipes/577058/ by Kent Milfeld
# @todo  Write our own version (don't like Capital Letter default: [y/N] )
#        original function definition: def query_yes_no(question, default="yes"):

def ask_yorn_question(question, default="yes"):
    """Ask a yes/no question via raw_input() and return their answer.

    "question" is a string that is presented to the user.
    "default" is the presumed answer if the user just hits <Enter>.
        It must be "yes" (the default), "no" or None (meaning
        an answer is required of the user).

    The "answer" return value is True for "yes" or False for "no".
    """
    valid = {"yes": True, "y": True, "ye": True,
             "no": False, "n": False}
    if default is None:
        prompt = " [y/n] "
    elif default == "yes":
        prompt = " [Y/n] "
    elif default == "no":
        prompt = " [y/N] "
    else:
        raise ValueError("invalid default answer: '%s'" % default)

    while True:
        sys.stdout.write(question + prompt)
        choice = raw_input().lower()
        if default is not None and choice == '':
            return valid[default]
        elif choice in valid:
            return valid[choice]
        else:
            sys.stdout.write("Please respond with 'yes' or 'no' "
                             "(or 'y' or 'n').\n")

#                          TACC addition  2015-04-30    Kent

#-------------------------------------------------------------------------------



## Ask to select question via raw_input() and return their answer.
#
# @parm res_list --  a list of reservations of the user
# @parm  default --  index of default reservation, -1 == none
#
# "default" is the selection if the user just types <Enter>.

def select_reservation(res_list, default=-1):

  if default == -1:
    prompt = " Enter # [no default] : "
  else:
    prompt = " Enter # [default %d] : " % (default + 1)

  print "Select the number of the reservation item:"

  while True:

    # List reservations with a selection number (index + 1)
    list_reservations(res_list)

    # Get response from user (choice is a string)
    sys.stdout.write(prompt)
    choice = raw_input()
    print ""

    # Action on user selection (choice)

    #   Not a number and not ""  -- handle no default case in else below
    if not is_int(choice) and not choice == "" :
      print "Please respond with a number (#) or return (default): "

    #   integer response
    if is_int(choice):
      int_choice = int(choice)
      if int_choice <= len(res_list) and int_choice > 0:
        return int_choice - 1
      else:
        print "The number %d is not in the list, try again." % int_choice
            
    #  return response  (handles return on no-default)
    else:
      if choice == "":

        if default == -1:
          print "You must respond with a number (#) only, or ctrl C to abort."
        elif default < len(res_list) and int_choice >= 0:
          return default

#-------------------------------------------------------------------------------



## print reservations with a header (labels)
#

def list_reservations(res_list):
  res_len = len(res_list)
  print "%3s %8s %12s  %-19s %s" % ("#", "Status", "queue", "StartTime ", "Name")
  for i in range( res_len):
    print "%3d %8s %12s  %19s %s" % \
          (i+1, res_list[i][4], 
                res_list[i][2], 
                res_list[i][1].replace('StartTime=',''), 
                res_list[i][0],)

#----------------------------------------------------------------------------



## Tests
#    select_reservation
#    ask_yorn_question
#
if __name__ == "__main__":

    #      Create list of reservations.  
    x0 = []
    x1 = []
    x0 = ["TACC-Training-2015-05-04", "StartTime=2015-05-04T08:00:00", "normal-mic",
          "jasona,milfeldt,spt6655,ling,jame84,jcrob,khp339","ACTIVE" ]
    x1 = ["TACC-Training-2015-05-05", "StartTime=2015-05-04T08:00:00", "normal-mic",
          "jasona,milfeldt,spt6655,ling,jame84,jcrob,khp339","INACTIVE" ]

    user_res = []
    user_res.append(x0)
    user_res.append(x1)

    #      Check reservation selection.
    selected_no = select_reservation(user_res, 1)
    print "selected number is: ",selected_no + 1

    print " ----------------------------\n"

    #      Check Yes or No question
    yorn = ask_yorn_question("Are you OK","no")
    print "Yes or No response: %s ", yorn

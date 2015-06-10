#!/usr/local/bin/python
#!/opt/apps/intel13/python/2.7.9/bin/python

## 
#  User Interaction and Query functions 
#  @file ask.py
#  @author Kent Milfeld
#  @date 2015-05-07
#  @note TACC
#  @copyright License
#
#
#  Detailed description
#  ask_yesno_question stolen from http://code.activestate.com/recipes/577058
#  @todo  Write our own version (don't like Capital Letter default: [y/N] )

import sys

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

def is_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False

## 
#  ask_yesno_question -- prompts user for yes/no answer
#
#  Stolen from http://code.activestate.com/recipes/577058/ by Kent Milfeld
#  @todo  Write our own version (don't like Capital Letter default: [y/N] )
#         original function definition: def query_yes_no(question, default="yes"):

def ask_yesno_question(question, default="yes"):
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



## 
#  Ask to select reservation via raw_input() and return their answer.
#
#  @param res_list --  a list of reservations of the user
#  @param  default --  index of default reservation 
#                      None, user can only select a reservation, or abort
#                      -1,   return means no reservation selected
#                      
#  @return         --  index of reservation or None (nothing selected)
#
#  "default" is the selection if the user just types <Enter>.
#

def select_reservation(res_list, default=None):

  if default is None:
    prompt       = " Enter # [no default] : "
    respond_with = " Respond with a number (#) or abort (^C): "

  elif default is -1:
    prompt       = " Enter # [or return = don't use reseration] : "
    respond_with = " Respond with a number (#), return [don't use a reservation] or abort (^C): "

  else:
    prompt = " Enter # [return = default %d] : " % (default + 1)
    respond_with = " Respond with a number (#), return [default #] or abort (^C): "

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

      print respond_with

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

        if default is None:
          print "You must respond with a number (#) only, or abort (^C)."
        if default < len(res_list) and default >= 0:
          return default
        if default is -1:
          return None

#-------------------------------------------------------------------------------



## 
#  list_revervations -- print reservations (from MyReservations class) 
#                       with a header (labels)
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



## 
#  ask Unit Test
#    select_reservation
#    ask_yesno_question
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
    print " Reservation Select----------------------------\n"
    selected_no = select_reservation(user_res, None)
    print "selected number is: ",selected_no + 1

    print " Reservation Select----------------------------\n"

    selected_no = select_reservation(user_res, 1)
    print "selected number is: ",selected_no + 1

    print " Reservation Select----------------------------\n"

    selected_no = select_reservation(user_res, -1)
    print "selected number is: ",selected_no

    print " Yes or No Question----------------------------\n"

    #      Check Yes or No question
    yorn = ask_yesno_question("Are you OK","no")
    print "Yes or No response: %s ", yorn

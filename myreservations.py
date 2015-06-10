#!/opt/apps/intel13/python/2.7.9/bin/python
#!/usr/local/bin/python

## 
#  Core Components for Working with MyReservations
#  @file Reservations.py
#  @author Kent Milfeld
#  @date 2015-05-07
#  @note TACC
#  @copyright License
#
#

#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

# System Modules

import subprocess
import os
import re
import ask

## 
#  Class MyReservations --Creates User Reservation List & Drives Res. Selection
#
#  @param user --  username 
#
#  Detailed description
#    initialization       -- sets default values for instance
#    get_my_reservations  -- creates user_res list from reservation, 
#                            specifies r options.
#    select_a_reservation -- creates user res. list, specifies r options.
#     
#    
#   Instance variables  
#     User Reservations info:
#       has_active, has_inactive, active_count, inactive_count
#       user_res -- list of user's reservations
#      
#     User Selected Reservation:
#       name, queue, project, status, start_time, list_no, use_reservation
#       list_no  -- selected reservation
  

class MyReservations(object):


  ## 
  #  Constructor -- set up defaults for instance variables
  #
  #  Detailed Description
  #    Instance variables are either 0, FALSE, None.  

  def __init__(self):

    #  Reservation Lists

    self.user_res = []        #This is an class attribute.
  
    #  Reservation has Active/Inactive, and rservation counts
  
    self.has_active     = False
    self.has_inactive   = False
    self.active_count   = 0
    self.inactive_count = 0
    self.count          = 0
  
    #  Basic reservation variables.
    #    Needed for job submissions:
    #      [name, queue, project]
    #      Project may not be defined
    #      Queue may not be defined, slurm returns '(null)'--> idev uses "none"
    #      All variables should equal None/False if no reservation found.
    #      Usual case: queue name provided and project not provided; also
    #                  status must be either ACTIVE or INACTIVE. 
    #    Informational:
    #      [status, start_time, list_no, use_reservation]
    #      status is ACTIVE or INACTIVE
    #      start_time  date and time when reservation is allowed to start
    #      list_no     0-n, where n+1 is the number of reservations for user
    #                  This is the number of the reservation to be used.
    #      use_reservation  Convenience variable.
    #
    #    returns
    #      determine_my_reservation
    #        True/False  Use or not use one of the reservation
    #                    list_no contains reservation to use if True
    #                    + Submission required and Information vars set.
  
    self.name            = None
    self.queue           = None
    self.project         = None
    self.status          = None
    self.start_time      = None
    self.list_no         = None
    self.use_reservation = False
  
  
    #  Reservation option information (named reservation, find my reservation)
    #     -r          == look for my reservation 
    #     -r <name>   == use this reservation
    #     -r none     == don't bother with look for reservation
  
    self.ropt_name       = None
    self.has_ropt        = False
    self.has_ropt_find   = False
    self.has_ropt_name   = False
    self.has_ropt_avoid  = False
    self.found_ropt_find = False
    self.found_ropt_name = False
  
  #-------------------------------------------------------------------------------
  
  ## 
  # get_my_reservations -- get reservations of user; set -r option requested.
  #
  # @param user -- idev user
  #
  # Detailed Description
  #
  #   get list of all Reservations
  #   Reservations are stored in double arrays:
  #   [ [name, start_time, partition, users, state], [name, start_time2...]]
  #
  #   parse for user name in Reservations list and locally store in user_res.
  #   set find, name, and avoid "has_ropt" variable from argument parsing.
  #   
  #   set find, name, and avoid "has_ropt" variable from argument parsing.
  #
  #   return True if user has reservations, has ropt_name, or has ropt_find.
  #   return False all other cases -- no need to thing about resevations.
  #

  def get_my_reservations(self, user):

    # Determine what -r option wants to do
    #if parse_args.idev_reservation is not None:

    if True is not None:
      self.has_ropt = True
      if parse_args.reserv_name is None:
        has_ropt_find = True
      else:
        self.ropt_name = parse_args.reserv_name
        if parse_args.reserv_name is "none":    #This should be None
           self.has_ropt_avoid = True
 
    # get reservation
    # pick up Jason's stuff.
    #user_res = Jason(socket_it_to_me)
  

    for i,a_res in enumerate(self.user_res):

      if "INACTIVE" in a_res:
        self.inactive_count += 1
        self.has_inactive = True
      else:
        self.active_count   += 1
        self.has_active   = True
        self.list_no = i

      if self.has_ropt_name:
        if self.ropt_name in a_res:        #Could use exact field here.
          self.found_ropt_name = True
          self.list_no = i

      if "'(null)'" in a_res:              #Fix up '(null)' == none
        self.user_res[i][2] = "none"       #Maybe use "None" here.

    self.count = self.active_count + self.inactive_count     
    if len(self.user_res) != self.count :
      print "raise and error here."

    if( self.count > 0 or self.has_ropt_find  or self.has_ropt_name ):

      return True
    else:
      return False
     
  #-------------------------------------------------------------------------------

  ## 
  # Evaluates with feedback from user, and -r options, which reservation to use.
  #   Solicits a user response when necessary or appropriate
  #   Provides reservation FYI when prudent for user to know
  #   Allows users to quit idev when they don't want/need to continue 
  #
  #   Uses ask module to solicit a response from user.
  #   Helper ask_ functions set up question input and info for ask Solicitation.
  #
  # @param -- no parameters (uses user name and -r option values)
  #
  #  
    
  def select_a_reservation(self):

    # 1 reservation case
    if(self.count == 1):

      # -r name  option used
      if self.has_ropt_name:

        if self.found_ropt_name:
          self.list_no=0 
          self.use_reservation = True
          return True
        else:
          #
          print " We did NOT find a reservation named ",self.ropt_name,"."
          print " But, we found   a reservation named ",self.name,"."
          if self.inactive_count is 1:
            torf = self.ask_to_use_inactive_res(self.name, self.start_time)
          else:
            self.torf = self.ask_to_use_active_res(self.name)
          if torf is True:
            self.list_no=0 
            self.use_reservation = True
            return torf
          else:
            os._exit(1)

      # -r  option used
      if self.has_ropt_find :

        # found an inactive res
        if(self.inactive_count == 1):
          torf = self.ask_to_use_inactive_res(self.name, self.start_time)
          if torf:
            self.list_no=0
            self.use_reservation = True
            return True
          else:
            os._exit(1)

        # found an active res
        else:                                        #must have 1 active
          self.list_no=0 
          self.use_reservation = True
          return True

      # no -r name  option
      if self.has_ropt == False :
        if(self.inactive_count == 1):
          print "FYI:  We found an INACTIVE reservation for you named: ",self.name
          print "      Use -r ",self.name," if you want to use and wait for it"
          print "      The reservation won't be available until: ", self.start_time
          use_reservation = False
          return False
        else:
          torf = self.ask_to_use_active_res(self.name)
          if torf:
            self.list_no=0 
            self.use_reservation=True
            return True
          else:
            self.use_reservation=False
            return False

    # 2 or more reservations cases
    else:

      # -r name  option
      if self.has_ropt_name:
           
        if self.found_ropt_name:

          # list_no was set in the init.
          self.use_reservation=True
          return True
        else:

          print " We did NOT find a reservation named ",self.ropt_name,"."
          print " We did find other reservations that you might care to use."
          if self.inactive.count > 0:
              print " INACTIVE reservations will not be available until the listed start_time."
              if self.active.count is 1:
                 default=self.list_no
              else:
                 default=None
              self.list_no=ask_to_use_1_res(self,default)
              self.use_reservation = True
              return torf

      # -r  option used (no argument)
      if self.has_ropt_find:
         
        if self.active_count is 1 :
          # list_no was set in the init.
          self.use_reservation = True
          return True

        if self.active_count is 0 : 
          print " Idev only found INACTIVE reservations for you."
          self.list_no = self.ask_to_use_1_res(self.user_res, None)
          self.use_reservation = True
          return True

        print " Idev found ",self.active_count," ACTIVE reservations."
        if (self.inactive_count > 0) :
          print "Idev found ",self.inactive_count," INACTIVE reservations."
          self.list_no = self.ask_to_use_1_res(self.user_res, None)
          self.use_reservation = True
          return True

      # no -r  option used
      if self.has_no_ropt:

        if self.active_count is 0 :

          print "FYI:  We found ",self.inactive_count," INACTIVE reservations for you."
          print "      Use -r reservation_name if you want to use and wait for it"
          print "      The reservation won't be available until start_time."

          # List reservations with a selection number (index + 1)
          ask.list_reservations(self.user_res)
          use_reservation = False

          return False

        elif self.active_count is 1 :

          # List reservations with a selection number (index + 1)
          print "FYI:  Idev found multiple reservations for you.  They are:"
          ask.list_reservations(self.user_res)

          print "Idev found an ACTIVE reservation for you."
          self.torf = self.ask_to_use_active_res(self.name)
          if torf is True:
            # list_no was set in the init.
            self.use_reservation = True
            return torf
          else:
            self.use_reservation = False
            return False

        else:
           print "Idev found multiple ACTIVE reservations."
           if self.inactive.count > 1:
             print " INACTIVE reservations were also found."
             print " INACTIVE reservations will not be available until the listed start_time."
           self.list_no = self.ask_to_use_1_res(self.user_res, -l)  


  #-------------------------------------------------------------------------------

  def ask_to_use_inactive_res(self, res_name, start_time):
    print " Idev Found 1 INACTIVE reservation for you: ", res_name, "."
    print " The reservation will not start until after ", start_time, "."
    torf = ask.query_yes_no("Do you want to wait for this INACTIVE reservation","no")
    return torf

  #-------------------------------------------------------------------------------

  def ask_to_use_active_res(self, res_name):
    print " Idev Found 1 ACTIVE reservation for you: ", res_name,"."
    torf = ask.query_yes_no("Do you want to use this ACTIVE reservation","yes")
    return torf

  #-------------------------------------------------------------------------------

  def ask_to_use_1_res(self, default):
    print " Idev Found ",len(self.user_res), " reservations for you."
    index = ask.query_list("Select a number:",default)
    return index
   
   
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------

if __name__ == "__main__":
  user = "unit_test1"
  res=MyReservations()

  torf = res.get_my_reservations(user)   #True if user res exists, or -r, or -r <name>


  if torf:
    # All reservation situations will be resolved inside select_a_reservation. 

    use_a_res = res.select_a_reservation()

    # Free to go ahead and use a reservation or do normal idev 
  
#-------------------------------------------------------------------------------

#http://effbot.org/zone/python-list.htm   lists
#  Possible way to handle determine_my_reservation:
#  Use reservation:
#     Use reservation/Don't user reservation.
#     Use:  Cases:
#              name, queue, project, status 
#              yes   yes    None      act./inact.   Pickup project from default
#              yes   none   None      act./inact.   User must supply a queue, pickup default project
#  These members are needed for making for batch job and final 
#  information: list_no, queue, project, status, name, start}
#
#   if res.use_reservation 
#     if res.queue = "none"       use command line queue
#     else                        advise to see admin/ reverse node lookup
#                                 TODO, suggest a queue.
#     if res.project=None         use default
#     if res.status = "INACTIVE"  provide countdown (TODO)
#   else                          do normal 
#   @todo                         reservations wo queue: suggest possible queue
#   @todo                         INACTIVE res., do time countdown with wait update 

# os._exit() http://stackoverflow.com/questions/1187970/how-to-exit-from-python-without-traceback

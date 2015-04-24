#!/opt/apps/intel13/python/2.7.9/bin/python

import subprocess
import os
import re

class Reservations:
  """Reservations information is extracted from external call
     uses scontrol show res.
     Function my_reservations gets reservations of a specified user."""

#                 # On instantiation, set up and fill arrays
  def __init__(self):

    reo_names = re.compile(r'^ReservationName=') # Regular Expression (RE) obj
    reo_nodes = re.compile(r'^\s+Nodes=')
    reo_users = re.compile(r'^\s+Users=')

    self.names   = []
    self.start   = []
    self.nodes   = []
    self.nodecnt = []
    self.queue   = []
    self.users   = []
    self.status  = []
    self.actv_cnt   = 0
    self.inactv_cnt = 0
    self.total_cnt  = 0

    output=subprocess.check_output('scontrol show res',shell=True)

#                 Extract information from scontrol reseration output
#                          Sets of 3 sequential lines contain information 
#                          information for a single reservation. Line begine with:
#
#                 ReservationName=
#                    Nodes=
#                    Users=

    for line in output.split(os.linesep):
      names_m = reo_names.match(line)
      nodes_m = reo_nodes.match(line)
      users_m = reo_users.match(line)
      if( names_m ):
        names_line=re.search( r'ReservationName=([^\s]+)\s+StartTime=([^\s]+)',line)
        self.names.append(  names_line.group(1))
        self.start.append(  names_line.group(2))
      if( nodes_m ):
        nodes_line=re.search( r'^\s+Nodes=([^\s]+).*NodeCnt=([^\s]+).*PartitionName=([^\s]+)',line)
        self.nodes.append(  nodes_line.group(1))
        self.nodecnt.append(nodes_line.group(2))
        self.queue.append(  nodes_line.group(3))
      if( users_m ):
        users_line=re.search( r'^\s+Users=([^\s]+).*State=([^\s]+)',line)
        self.users.append(  users_line.group(1))
        self.status.append( users_line.group(2))

#               Determine total number of reservations, and in/active count.
    self.total_cnt = len(self.names)
    self.actv_cnt   = self.status.count("ACTIVE")
    self.inactv_cnt = self.status.count("INACTIVE")

#                                          # Create user_actv / usr_inactv arrays
#                                          # if user has reservation(s).
  def my_reservations(self,user):

    self.user = user

    p_user = re.compile(r'\b%s\b'%self.user)  # Use "breaks" around user. A jack search 
#                                               # distinguishes between jack and jackson

    self.user_name = user

    self.user_actv_cnt   = 0
    self.user_inactv_cnt = 0
    self.user_total_cnt  = 0

    sl=filter(p_user.search,self.users)   # find out if user is in any reservation
#                                           # filter: nifty way to find RE in arrays

    if( sl ):                             # need arrays only if user has a res.
      self.user_actv_names   = []
      self.user_actv_start   = []
      self.user_actv_nodes   = []
      self.user_actv_nodecnt = []
      self.user_actv_queue   = []
      self.user_actv_users   = []
      self.user_actv_status  = []
  
      self.user_inactv_names   = []
      self.user_inactv_start   = []
      self.user_inactv_nodes   = []
      self.user_inactv_nodecnt = []
      self.user_inactv_queue   = []
      self.user_inactv_users   = []
      self.user_inactv_status  = []
  
      reo_user = re.compile(r'\b%s\b'%user)         # create RE object

      for idx, user_list in enumerate(self.users):  # need index of array element
        user_m=reo_user.search(user_list)          # user match
        if( user_m ):
          if( self.status[idx] == "ACTIVE" ):
            print "something active"  , idx
            self.user_actv_names.append(   self.names[  idx] )
            self.user_actv_start.append(   self.start[  idx] )
            self.user_actv_nodes.append(   self.nodes[  idx] )
            self.user_actv_nodecnt.append( self.nodecnt[idx] )
            self.user_actv_queue.append(   self.queue[  idx] )
            self.user_actv_users.append(   self.users[  idx] )
            self.user_actv_status.append(  self.status[ idx] )
          if( self.status[idx] == "INACTIVE" ):
            print "something inactive"  , idx
            self.user_inactv_names.append(   self.names[  idx] )
            self.user_inactv_start.append(   self.start[  idx] )
            self.user_inactv_nodes.append(   self.nodes[  idx] )
            self.user_inactv_nodecnt.append( self.nodecnt[idx] )
            self.user_inactv_queue.append(   self.queue[  idx] )
            self.user_inactv_users.append(   self.users[  idx] )
            self.user_inactv_status.append(  self.status[ idx] )

      self.user_actv_cnt   = len(self.user_actv_names)
      self.user_inactv_cnt = len(self.user_inactv_names)
      self.user_total_cnt  = self.user_actv_cnt + self.user_inactv_cnt


if __name__ == "__main__":
  res=Reservations()
  print "R.names",res.names
  print "R.status",res.status
  print "R.total_cnt",res.total_cnt
  print "R.actv_cnt",res.actv_cnt
  
  res.my_reservations("cazes")

  print "R res_cnt,   active_cnt names  ",res.user_total_cnt, res.user_actv_cnt,   res.user_actv_names
  print "R res_cnt, inactive_cnt names  ",res.user_total_cnt, res.user_inactv_cnt, res.user_inactv_names

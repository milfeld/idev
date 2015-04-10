#!/opt/apps/intel14/mvapich2_2_0/python/2.7.6/bin/python

import subprocess
import os
import re

class Project:
  """Gathers project information
      instantiation 
        no default projects--> idev_none   
        default project --> use it:     (if inactive at sbatch, handle there)
        if project list   --> idev_project_list
                          ( sets default_project)(set up selection array if list)  

     get_projects() member function:  get projects and active/inactive status
        called if default projects == idev_none
        called if project list     == idev_project_list (check for activity)

      project_select() 
        called only if a default project is not known, or project list exists
        if multiple default projects -- ask user to select one
        if no default project exists
        requests user to select a default project or select from multiple projs.

   """
#                          #On instantiation, set up and fill arrays
  def __init__(self,rc):

    self.rc = rc
    if(rc.proj_default_status == "has_default"):
        self.project_name = rc.proj_default   #should this be global?
      self.select_project = "no"
    else:
      self.select_project = "yes"

    #output=subprocess.check_output('cat $HOME/.idevrc',shell=True)

  def get_projects(self,user):
    self.user = user
    for line in output.split(os.linesep):
      default_m      = reo_proj_default.match(     line)
      default_old_m  = reo_proj_default_old.match( line)
      list_m         = reo_proj_list.match(        line)

      if(default_m or default_old_m ):
        default_line=re.search( r'\bidev_project\b\s+([^\s]+)\s*',line)
        self.proj_default        = default_line.group(1)
        self.proj_default_status = "has_default"

      if(list_m ):
        list_line=re.search( r'\bidev_project_list\b\s+(.*)\s*$',line)
        self.proj_list        = list_line.group(1).split('/,/')
        self.proj_list_status = "has_list"

#                                          # Create user_actv / usr_inactv arrays
#                                          # if user has reservation(s).
  def get_projects(self,user):

    self.proj_user = user
    projectuser_map = "/usr/local/etc/project.map"
    import pw
    self.uid = pwd.getpwname(self.user).pw_uid

    reo_proj = re.compile(r'^\S\s+(\d+)\s*$') 
    output=subprocess.check_output('cat /usr/local/etc/project.map',shell=True)

    for line in output.split(os.linesep):
      proj_m = reo_proj.match(line)
      if(proj_m)    

#  p_user = re.compile(r'\b%s\b'%self.user)  # Use "breaks" around user. A jack search 
#                                               # distinguishes between jack and jackson

#    sl=filter(p_user.search,self.users)   # find out if user is in any reservation
#                                           # filter: nifty way to find RE in arrays


if __name__ == "__main__":
  rc=Idevrc()
  print "RUNCOM proj default status ",rc.proj_default_status
  if( rc.proj_default_status == "has_default"): print "RUNCOM proj default",rc.proj_default
  print "RUNCOM proj list status ",rc.proj_list_status
  if( rc.proj_list_status == "has_list")   : print "RUNCOM proj list   ",rc.proj_list

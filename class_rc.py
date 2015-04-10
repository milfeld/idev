#!/opt/apps/intel14/mvapich2_2_0/python/2.7.6/bin/python

import subprocess
import os
import re

class Idevrc:
  """Gathers default values from $HOME/.idevrc RUNCOM (RC) file
        Default Sentinels:   syntax
           project           string (project name)
           project_list      space separated strings (proj. names)
           time              integer (seconds)
           queue             string (valid queue name)
                               or user has a selection list
                              return value
        THIS CLASS DOES NOT CHECK FOR "CORRECTNESS" OF DEFAULT VALUES.
   """

  idevrc_default_names    = ['idev_project', 'idev_project_list', 'idev_time', 'idev_queue' ]

#                          #On instantiation, set up and fill arrays
  def __init__(self):

    reo_proj_default      = re.compile(r'idev_project_default') # Regular Expression (RE) obj
    reo_proj_list         = re.compile(r'idev_project_list')
    reo_time              = re.compile(r'idev_time')
    reo_queue             = re.compile(r'idev_queue')

    self.proj_default     = "none"
    self.proj_list        = []
    self.time             = "none"
    self.queue            = "none"


    self.proj_default_status     = "none"
    self.proj_list_status        = "none"
    self.time_status             = "none"
    self.queue_status            = "none"

#     eventually put this in class RC

    output=subprocess.check_output('cat $HOME/.idevrc',shell=True)

#                         Extract Resource Control (RC) from $HOME/.idevrc
#                         Resource options:
#                            idev_project
#                            idev_project_list

    for line in output.split(os.linesep):
      default_m      = reo_proj_default.match( line )
      list_m         = reo_proj_list.match(    line )
      time_m         = reo_time.match(         line )
      queue_m        = reo_queue.match(        line )

      if( default_m ):
        default_line=re.search( r'\bidev_project\b\s+([\S]+)\s*',line )
        self.proj_default        = default_line.group(1)
        self.proj_default_status = "has_default"

      if( list_m ):
        list_line=re.search( r'\bidev_project_list\b\s+(.*)\s*$',line )
       #list_line=re.search( r'\bidev_project_list\b\s+([^#])\s*$',line )
        self.proj_list        = list_line.group(1).split('/,/')
        self.proj_list_status = "has_list"

      if( time_m ):
        time_line=re.search( r'\bidev_time\b\s+([^\s]+)\s*',line )
        self.time        = time_line.group(1)
        self.time_status = "has_time"

      if( queue_m ):
        queue_line=re.search( r'\bidev_queue\b\s+([^\s]+)\s*',line )
        self.queue        = queue_line.group(1)
        self.queue_status = "has_queue"

    # put_default(self,default_name, default_value):

if __name__ == "__main__":
  rc=Idevrc()

  if( bool(1)                                ): print "RUNCOM proj default status ", rc.proj_default_status
  if( rc.proj_default_status == "has_default"): print "RUNCOM proj default        ", rc.proj_default

  if( bool(1)                                ): print "RUNCOM proj list    status ", rc.proj_list_status
  if( rc.proj_list_status    == "has_list"   ): print "RUNCOM proj list           ", rc.proj_list

  if( bool(1)                                ): print "RUNCOM      time    status ", rc.time_status
  if( rc.time_status         == "has_time"   ): print "RUNCOM      time           ", rc.time

  if( bool(1)                                ): print "RUNCOM     queue    status ", rc.queue_status
  if( rc.queue_status        == "has_queue"  ): print "RUNCOM     queue           ", rc.queue

from time import time, sleep
import click
import os

from .utils import read_json


'''
Data Structure

group hierarchy
  data-science -> bishop
  data-sceince -> kaggle
  coures -> physics
  coding-warmup

  query 
    - group: get progress by day, week, total

    day:
      two tables  
      1) allocated - per row display [group (top-level), progress bar, # comp / alloc] 
      2) unallocated - per row display [group (top-level), progress bar, # comp (relative to max item)]
    
    progress --week (arg = top-level group):
      one table
        no arg - row [group (top-level), progress bar, # comp / alloc]
          - proportion (%) tasks completed on time, extended complete, extended incomplete and deferred/incomplete (total)
        arg - row [group (secondary), progress bar, # comp (relative to max item)]
          - proportion (%) tasks completed on time, extended complete, extended incomplete and deferred/incomplete (group)
    
    progress --total (arg = top-level group):
      one table
        no arg - row [group (top-level), progress bar, # comp (relative to max item)]
          - proportion (%) tasks completed on time, extended complete, extended incomplete and deferred/incomplete (total)
        arg - row [group (secondary), progress bar, # comp (relative to max item)]
          - proportion (%) tasks completed on time, extended complete, extended incomplete and deferred/incomplete (group)
      prev 4 week graph [allocated, complete, task completion rate]

   task {
     complete: boolean, 
     extended: boolean, 
     paused: boolean, 
     group: string, 
     allocated_time: float, 
     end_tstamp: float, 
     paused_tstamp: float
   }

   task -> Groups 

   Groups (JSON)
   {
     group_A: {
       allocated: time,
       day: {tasks: int, completed: int, extended: int, elapsed: time},
       week: {tasks: int, completed: int, extended: int, elapsed: time},
       total: {tasks: int, completed: int, extended: int, elapsed: time},
       subgroups: {
         sgroup_AA: {
           day: {tasks: int, completed: int, extended: int, elapsed: time},
           week: {tasks: int, completed: int, extended: int, elapsed: time},
           total: {tasks: int, completed: int, extended: int, elapsed: time}
         },
         sgroup_AB: {
           day: {tasks: int, completed: int, extended: int, elapsed: time},
           week: {tasks: int, completed: int, extended: int, elapsed: time},
           total: {tasks: int, completed: int, extended: int, elapsed: time}
         }
       },
     },
    group_B: {
      alloacted: time
      day: {tasks: int, completed: int, extended: int, elapsed: time},
      week: {tasks: int, completed: int, extended: int, elapsed: time},
      total: {tasks: int, completed: int, extended: int, elapsed: time}
    }
   }
  

current task - started, ends, elapsed (updated by pause, resume, extend, defer, complete)
'''

class Tymebox(object):

  def __init__(self):
    self.dir         = click.get_app_dir('tymebox')
    self.groups_path = os.path.join(self.dir, 'groups')
    self.tasks_path  = os.path.join(self.dir, 'tasks')
    
    self.groups = read_json(self.groups_path, type=dict)
    self.tasks  = read_json(self.tasks_path, type=dict)

  def new_task_group(self):
    return {
      'allocated': None,
      'day':   {'tasks': 0, 'completed': 0, 'extended': 0, 'elapsed': 0},
      'week':  {'tasks': 0, 'completed': 0, 'extended': 0, 'elapsed': 0},
      'total': {'tasks': 0, 'completed': 0, 'extended': 0, 'elapsed': 0},
      'subgroups': None
    }

  def parse_days(self,scheduled_days):
    days = 'mtwrfsu'
    res = []
    for chunk in scheduled_days:
      start, end = days.index(chunk[0]), days.index(chunk[-1])
      for day in days[start:end + 1]:
        res.append(day)
    return res
  
  def parse_minutes(self,duration):
    hours, minutes = map(int,('0' + duration).split(':'))
    return hours * 60 + minutes

  def allocate(self, group, duration, days):
    minutes = self.parse_minutes(duration)
    scheduled = {day: minutes for day in self.parse_days(days)}
    self.groups[group] = self.groups.get(group, self.new_task_group())
    self.groups[group]['allocated'] = scheduled

  def remove(self, group):
    pass

  def sync(self):
    pass

  def update_group_data(self):
    task  = self.tasks['task']
    group = task['group']
    for interval in ['day', 'week', 'total']:
      group[interval]['tasks'] += 1
      group[interval]['complete'] += 1 if task['complete'] else 0
      group[interval]['extended'] += 1 if task['extended'] else 0
    
  def start(self, group, task, duration):
    if 'task' in self.tasks:
      self.update_group_data()
    
    dur_sec = self.parse_minutes(duration) * 60
    self.tasks['task'] = {
      'complete': False, 
      'extended': False, 
      'paused': False, 
      'group': group[0], 
      'allocated_time': dur_sec, 
      'end_tstamp': time() + dur_sec, 
      'paused_tstamp': None
    }
    print(self.groups)
    print(self.tasks)


  def save(self):
    pass








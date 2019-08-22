import click


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
      





current task - started, ends, elapsed (updated by pause, resume, extend, defer, complete)




'''
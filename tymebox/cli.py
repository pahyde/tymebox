from time import time, sleep
import click

from .tymebox import Tymebox
from .utils import progress_bar
from .utils import red, green, yellow, blue, magenta, cyan


@click.group()
@click.pass_context
def cli(ctx):
    '''
    A lightweight CLI application to plan and manage
    daily tasks while tracking long-term accomplishment
    '''
    ctx.obj = Tymebox()

#allocate and deallocate time requirements
@cli.command()
@click.argument('group', nargs=1)
@click.argument('duration', nargs=1)
@click.argument('days',nargs=-1)
@click.pass_obj
def allocate(tymebox, group, duration, days):
    '''Allocate time for new task group'''
    tymebox.allocate(group, duration, days)
    hr_time = human_readable_time(duration)
    hr_days = human_readable_days(days)
    message = '\n\nAllocated {} for task group {} on {}\n\n'
    click.echo(message.format(hr_time, blue(group), magenta(hr_days)))
    tymebox.save_group_data()

@cli.command()
@click.argument('group', nargs=1)
@click.pass_obj
def remove(group):
    '''Remove a task group'''
    tymebox.remove()


#start a task
@cli.command()
@click.argument('group', nargs=-1)
@click.argument('task', nargs=1)
@click.argument('duration',nargs=1)
@click.pass_obj
@click.pass_context
def start(ctx, tymebox, group, task, duration):
    '''Start a new task!'''

    if tymebox.has_running_task():

        status = tymebox.current_task_status()
        message = '\n{} remaining for unresolved task "{}" - {}\n'
        click.echo(message.format(parse_hms(int(status['time_remaining'])), status['task'], status['group']))
        click.echo('input "c" to mark ' + cyan('complete') + ', "d" to mark ' + blue('deferred') + ', or "q" to exit')
        
        userin = input()

        if   userin == 'c': ctx.invoke(complete, tymebox)
        elif userin == 'd': ctx.invoke(defer, tymebox)
        else              : return
        
    tymebox.start(group, task, duration)
    tymebox.save()
    click.echo('Started {} task {} at {}'.format(group, task, duration, time()))


#observe and managage running task
@cli.command()
def pause():
    '''pause a running task'''

@cli.command()
def resume():
    '''resume a paused task'''


@cli.command()
def status():
    '''View task status and progress in real-time'''

@cli.command()
def close():
    '''Terminate real-time status update process'''

#update state of running task [duration, tags] (tags: complete, incomplete, in-progress)
@cli.command()
@click.pass_obj
def complete(tymebox):
    '''
    manually tags running or previous task complete. if running, task is ended.
    tasks which run out their allotted time are tagged complete by default.
    '''
    if not tymebox.has_running_task():
        click.echo(red("\nNo task started.\n") + "\nStart a task with" + cyan(" tymebox start [group] [duration]\n"))
        return

    status = tymebox.current_task_status()

    if status['time_remaining'] != 0:
        time_remaining = red(parse_hms(int(status['time_remaining'])))
        task = magenta(status['task'])
        group = cyan(status['group'])
        click.echo('\n{} remaining for task {} - {}\n'.format(time_remaining, task, group))
        click.echo('mark task complete? (y/n):')
        if input().lower() != 'y': return 

    tymebox.complete()
    tymebox.save()
    click.echo('\n{} - {} complete!\n'.format(status['task'],status['group']))


def parse_hms(s):
    zero_fill = lambda t: str(t) if t > 9 else '0{}'.format(t)

    hours, minutes, seconds = s // 3600, (s % 3600) // 60, s % 60
    return '{}:{}:{}'.format(*(zero_fill(t) for t in [hours, minutes, seconds]))



@cli.command()
@click.pass_obj
@click.argument('extension', nargs=1)
def extend(tymebox, extension):
    '''
    extends allotted time by given amount for running
    or previously ended task.
    '''
    if not tymebox.has_running_task():
        click.echo("\nNo task available to extend. \nStart a task with tymebox start [group] [duration]\n")
        return
    
    tymebox.extend(extension)
    tymebox.save()
    
    status = tymebox.current_task_status()

    time_remaining = parse_hms(int(status['time_remaining']))
    task           = magenta(status['task'])
    group          = blue(status['group'])

    message = '\nExtended task by {}. {} remaing for task {} - {}\n'
    click.echo(message.format(human_readable_time(extension),time_remaining, task, group))
     


@cli.command()
def defer():
    '''
    tags running or previously ended task incomplete.
    if task was running, only the elapsed time is saved to records.
    '''
    tymebox.defer()
    tymebox.save()
    click.echo('{} - {} defered'.format(status['task'],status['group']))



#long-term stats
@cli.command()
def incomplete():
    '''dispays list of incomplete tasks'''

@cli.command()
def today():
    '''
    View current progress on allocated tasks for the day.
    Progress also displayed for unallocated tasks started during the day.
    '''

@cli.command()
@click.option('--week',  'scale', flag_value='week')
@click.option('--total', 'scale', flag_value='total')
def progress(scale):
    '''View in depth progress on all task groups or any one in particular.'''


def human_readable_time(time):
    hours, minutes = map(int,('0'+time).split(':'))
    return cyan('{} hour(s)'.format(hours)) + ' and ' + cyan('{} minute(s)'.format(minutes))

def human_readable_days(days):
    expand = {
        'm': 'Monday',
        't': 'Tuesday',
        'w': 'Wednesday',
        'r': 'Thursday',
        'f': 'Friday',
        's': 'Saturday',
        'u': 'Sunday',
        '-': ' - ',
    }
    days = [''.join(expand[c] for c in day) for day in days]
    return ', '.join(days[:-1]) + ' and ' + days[-1] if len(days) > 1 else days[0]

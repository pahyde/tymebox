from time import sleep
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
def start(tymebox, group, task, duration):
    '''Start a new task!'''
    tymebox.sync()
    tymebox.start(group, task, duration)
    tymebox.save_task_data()
    tymebox.save_group_data()
    click.echo('group: {}\ntask: {}\nduration: {}'.format(group, task, duration))

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
def complete():
    '''
    manually tags running or previous task complete. if running, task is ended.
    tasks which run out their allotted time are tagged complete by default.
    '''

@cli.command()
def extend():
    '''
    extends allotted time by given amount for running
    or previously ended task.
    '''

@cli.command()
def defer():
    '''
    tags running or previously ended task incomplete.
    if task was running, only the elapsed time is saved to records.
    '''


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

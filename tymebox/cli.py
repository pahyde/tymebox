from .tymebox import Tymebox
import click


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
    click.echo('allocated group: {}'.format(group))
    tymebox.save()

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
def start(group, task, duration):
    '''Start a new task!'''
    tymebox.start(group, task, duration)
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

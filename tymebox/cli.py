import click


@click.group()
@click.pass_context
def cli(ctx):
    '''
    A lightweight CLI application to plan and manage
    daily tasks while tracking long-term accomplishment
    '''

#allocate and deallocate time requirements
@cli.command()
@click.argument('group', nargs=1)
@click.argument('duration', nargs=1)
@click.argument('days',nargs=-1)
def allocate(group, duration, days):
    '''Allocate time for new task group'''
    click.echo('group: {}\nduration: {}\ndays: {}'.format(group, duration, days))

@cli.command()
@click.argument('group', nargs=1)
def remove(group):
    '''Remove a task group'''


#start a task
@cli.command()
@click.argument('group', nargs=-1)
@click.argument('task', nargs=1)
@click.argument('duration',nargs=1)
def start(group, task, duration):
    '''Start a new task!'''
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
@click.option('--month', 'scale', flag_value='month')
@click.option('--total', 'scale', flag_value='total')
def progress(scale):
    '''View in depth progress on all task groups or any one in particular.'''

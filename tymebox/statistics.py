from time import time, sleep
from .utils import red, green, yellow, blue, cyan, magenta



def progress_bar(num, den):
    block    = u'\u258C'
    progress = min(100, num / den * 100)
    return '[ ' + block * int(progress/2) + '-' * (50 - int(progress/2)) + ' ] ' + '{0:.2f} %'.format(progress) + ' ' * (3 - len(str(int(progress))))
 


def tabulated_days_progress(rows):

    group_width = max(len(row[0]) for row in rows) + 2
    justify = lambda row: row + ' ' * (group_width - len(row))

    divider = '\n+{}+{}+\n'.format('-' * (group_width + 2), '-' * 65)
    table = divider.join('| {} | {} |'.format(justify(row[0]), progress_bar(row[1],row[2])) for row in rows)

    return divider + table + divider



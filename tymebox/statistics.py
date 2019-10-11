from time import time, sleep
from .utils import red, green, yellow, blue, cyan, magenta



def progress_bar(num, den):
    block    = u'\u258C'
    progress = num / den * 100
    return '\n[ ' + block * int(progress/2) + '-' * int(50 - progress/2) + ' ] ' + '{0:.2f} %\n'.format(progress) 
 









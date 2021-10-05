### util.py ###################################
# Commonly used functions, classes are defined in here
###############################################


from env import *
from config import *


### lambda functions
tprint     = lambda dic: print(tabulate(dic, headers='keys', tablefmt='psql'))  # print 'dic' with fancy 'psql' form
list_anys  = lambda path: [(join(path, name), name) for name in sorted(os.listdir(path))]
list_dirs  = lambda path: [(join(path, name), name) for name in sorted(os.listdir(path)) if isdir(join(path, name))]
list_files = lambda path: [(join(path, name), name) for name in sorted(os.listdir(path)) if isfile(join(path, name))]


class PATH:
    ROOT   = abspath(dirname(dirname(__file__)))
    INPUT  = join(ROOT, 'input')
    OUTPUT = join(ROOT, 'output')
    SRC    = join(ROOT, 'src')
    TRAIN  = join(INPUT, 'train')
    TEST   = join(INPUT, 'test')

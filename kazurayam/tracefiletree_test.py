import os
from pathlib import Path
from . import fileutils
from . import tracefiletree


def test_trace(basedir):
    wt = os.path.join(basedir, 'test_trace')
    fileutils.init_dir(wt)
    os.chdir(wt)
    f = fileutils.write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)
    #
    #print('\n{}'.format(wt))
    starting_dir = Path(wt)
    main = tracefiletree.TraceMain(starting_dir)
    result = main.trace()
    #print(result)


def test_excludes(basedir):
    wt = os.path.join(basedir, 'test_excludes')
    fileutils.init_dir(wt)
    os.chdir(wt)
    f = fileutils.write_file(wt, 'src/greeting', 'Hello, world!\n')
    b = fileutils.write_file(wt, 'build/greeting.exe', 'Executable!\n')
    #
    #print('\n{}'.format(wt))
    starting_dir = Path(wt)
    main = tracefiletree.TraceMain(starting_dir, ['build'])
    result = main.trace()
    #print(result)


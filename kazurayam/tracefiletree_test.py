import os
from io import StringIO
from pathlib import Path
from fileutils import init_dir, write_file
from tracefiletree import TraceMain


def test_smoke(basedir):
    wt = os.path.join(basedir, 'test_smoke')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)
    #
    print('\n{}'.format(wt))
    starting_dir = Path(wt)
    main = TraceMain(starting_dir)
    result = main.trace()
    print(result)

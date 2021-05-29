import os
from pathlib import Path
from fileutils import init_dir, write_file
from graphvizfiletree import GraphvizMain


def test_graph(basedir):
    wt = os.path.join(basedir, 'test_graph')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)
    #
    print('\n{}'.format(wt))
    starting_dir = Path(wt)
    main = GraphvizMain(starting_dir)
    result = main.draw()
    print(result)

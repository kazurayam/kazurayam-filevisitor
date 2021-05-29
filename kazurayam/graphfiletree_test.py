import os
import pytest
from pathlib import Path
from fileutils import init_dir, write_file
from filevisitor import Files
from graphfiletree import GraphFileTreeVisitor


def test_graph(basedir):
    wt = os.path.join(basedir, 'test_graph')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)
    #
    print('\n{}'.format(wt))
    starting_dir = Path(wt)
    crawler = GraphFileTreeVisitor(starting_dir)
    Files.walk_file_tree(starting_dir, crawler)

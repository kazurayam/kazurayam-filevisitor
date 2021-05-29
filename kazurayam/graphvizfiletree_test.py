import os
from pathlib import Path
from fileutils import init_dir, write_file
from graphvizfiletree import GraphvizMain
from graphviz import Digraph


def test_graph(basedir):
    wt = os.path.join(basedir, 'test_graph')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)
    #
    starting_dir = Path(wt)
    main = GraphvizMain(starting_dir)
    g: Digraph = main.draw()
    print(g.source)
    g.render("test_graph")

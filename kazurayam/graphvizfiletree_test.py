import os
from pathlib import Path
from fileutils import init_dir, write_file
from graphvizfiletree import GraphvizMain
from graphviz import Digraph
import fnmatch


def test_graph(basedir):
    wt = os.path.join(basedir, 'test_graph')
    init_dir(wt)
    os.chdir(wt)
    write_file(wt, '.gitignore', '*~\n')
    write_file(wt, 'README.md', 'A sample FileTree graph')
    write_file(wt, 'src/greeting', 'Hello, world!\n')
    write_file(wt, 'src/hello.pl', 'print(\"Hello, world!\")\n')
    write_file(wt, "tmp/.cache/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", "this is a fake")
    #
    main = GraphvizMain(Path(wt))
    g: Digraph = main.draw()
    # print(g.source)
    g.render("test_graph", format="png")
    g.render("test_graph", format="pdf")
    assert os.path.exists("test_graph.pdf")


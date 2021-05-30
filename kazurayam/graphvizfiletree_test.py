import os
from pathlib import Path
from graphviz import Digraph
from . import fileutils
from . import graphvizfiletree


def test_graph(basedir):
    wt = os.path.join(basedir, 'test_graph')
    fileutils.init_dir(wt)
    os.chdir(wt)
    fileutils.write_file(wt, '.gitignore', '*~\n')
    fileutils.write_file(wt, 'README.md', 'A sample FileTree graph')
    fileutils.write_file(wt, 'src/greeting', 'Hello, world!\n')
    fileutils.write_file(wt, 'src/hello.pl', 'print(\"Hello, world!\")\n')
    fileutils.write_file(wt, "tmp/.cache/0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", "this is a fake")
    #
    main = graphvizfiletree.GraphvizMain(Path(wt))
    g: Digraph = main.draw()
    # print(g.source)
    g.render("test_graph", format="png")
    g.render("test_graph", format="pdf")
    assert os.path.exists("test_graph.pdf")


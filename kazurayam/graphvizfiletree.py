from io import StringIO
import os.path
from pathlib import Path
from filevisitor import FileVisitor, FileVisitResult, Files
from graphviz import Digraph

class GraphvizFileTreeVisitor(FileVisitor):

    def __init__(self, starting_dir: Path, g: Digraph):
        self.start = starting_dir
        self.g = g

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        relative_path = os.path.relpath(directory, self.start)
        self.buffer.write("> {}/\n".format(relative_path))
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, io_error: IOError) -> FileVisitResult:
        relative_path = os.path.relpath(directory, self.start)
        self.buffer.write("< {}/\n".format(relative_path))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        relative_path = os.path.relpath(file, self.start)
        self.buffer.write("= {}\n".format(relative_path))
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, io_error: IOError) -> FileVisitResult:
        relative_path = os.path.relpath(file, self.start)
        self.buffer.write("! {}\n".format(relative_path))
        return FileVisitResult.CONTINUE


class GraphvizMain:

    def __init__(self, starting_dir: Path):
        self.start = starting_dir
        self.buffer = StringIO()

    def draw(self):
        g = Digraph("main", comment="File Tree graph")
        g.attr('graph', laout="dot", rank="max", rankdir="LR", splines="ortho")
        g.node_attr.update(fontname="arial", fontsize="10")
        g.edge_attr.update(constraint="true", arrowhead="onormal")
        ##
        g.edge("A", "B")
        #visitor = GraphvizFileTreeVisitor(self.start, self.buffer)
        #Files.walk_file_tree(self.start, visitor)
        #result = self.buffer.getvalue()
        #self.buffer.close()
        ##
        return g


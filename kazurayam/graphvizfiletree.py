import os.path
from pathlib import Path
from graphviz import Digraph
from . import filevisitor


class GraphvizFileTreeVisitor(filevisitor.FileVisitor):

    def __init__(self, starting_dir: Path, g: Digraph):
        self.start = starting_dir
        self.g = g

    def pre_visit_directory(self, directory: Path) -> filevisitor.FileVisitResult:
        its_relative_path = os.path.relpath(directory, self.start)
        # self.buffer.write("> {}/\n".format(its_relative_path))
        self.g.node(its_relative_path, directory.name, shape="folder")
        self.g.node(its_relative_path + "_cp", "", shape="point", width="0")
        self.g.edge(its_relative_path, its_relative_path + "_cp", arrowhead="none")
        if directory is not self.start:
            parent_relative_path = os.path.relpath(directory.parent, self.start)
            self.g.edge(parent_relative_path + "_cp", its_relative_path + ":w")
        return filevisitor.FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, io_error: IOError) -> filevisitor.FileVisitResult:
        its_relative_path = os.path.relpath(directory, self.start)
        # self.buffer.write("< {}/\n".format(its_relative_path))
        return filevisitor.FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> filevisitor.FileVisitResult:
        its_relative_path = os.path.relpath(file, self.start)
        # self.buffer.write("= {}\n".format(its_relative_path))
        self.g.node(its_relative_path, file.name)
        parent_relative_path = os.path.relpath(file.parent, self.start)
        self.g.edge(parent_relative_path + "_cp", its_relative_path + ":w")
        return filevisitor.FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, io_error: IOError) -> filevisitor.FileVisitResult:
        its_relative_path = os.path.relpath(file, self.start)
        # self.buffer.write("! {}\n".format(its_relative_path))
        return filevisitor.FileVisitResult.CONTINUE


class GraphvizMain:

    def __init__(self, starting_dir: Path, excludes=[]):
        self.start = starting_dir
        self.excludes = excludes

    def draw(self):
        g = Digraph("main", comment="File Tree graph")
        g.attr('graph', laout="dot", rank="max", rankdir="LR", splines="ortho",
               ranksep="0.5", nodesep="0.3")
        g.node_attr.update(shape="rectangle", height="0.3", fontname="arial", fontsize="10")
        g.edge_attr.update(constraint="true", arrowhead="onormal")

        visitor = GraphvizFileTreeVisitor(self.start, g)
        filevisitor.Files.walk_file_tree(visitor, self.start, self.excludes)

        return g

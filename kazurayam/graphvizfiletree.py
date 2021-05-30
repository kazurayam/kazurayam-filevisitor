import os.path
from pathlib import Path
from filevisitor import FileVisitor, FileVisitResult, Files
from graphviz import Digraph


class GraphvizFileTreeVisitor(FileVisitor):

    def __init__(self, starting_dir: Path, g: Digraph):
        self.start = starting_dir
        self.g = g

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        its_relative_path = os.path.relpath(directory, self.start)
        # self.buffer.write("> {}/\n".format(its_relative_path))
        self.g.node(its_relative_path, directory.name, shape="folder")
        self.g.node(its_relative_path + "_cp", "", shape="point", width="0")
        self.g.edge(its_relative_path, its_relative_path + "_cp", arrowhead="none")
        if directory is not self.start:
            parent_relative_path = os.path.relpath(directory.parent, self.start)
            self.g.edge(parent_relative_path + "_cp", its_relative_path + ":w")
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, io_error: IOError) -> FileVisitResult:
        its_relative_path = os.path.relpath(directory, self.start)
        # self.buffer.write("< {}/\n".format(its_relative_path))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        its_relative_path = os.path.relpath(file, self.start)
        # self.buffer.write("= {}\n".format(its_relative_path))
        self.g.node(its_relative_path, file.name)
        parent_relative_path = os.path.relpath(file.parent, self.start)
        self.g.edge(parent_relative_path + "_cp", its_relative_path + ":w")
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, io_error: IOError) -> FileVisitResult:
        its_relative_path = os.path.relpath(file, self.start)
        # self.buffer.write("! {}\n".format(its_relative_path))
        return FileVisitResult.CONTINUE


class GraphvizMain:

    def __init__(self, starting_dir: Path):
        self.start = starting_dir

    def draw(self):
        g = Digraph("main", comment="File Tree graph")
        g.attr('graph', laout="dot", rank="max", rankdir="LR", splines="ortho", ranksep="0.3", nodesep="0.2")
        g.node_attr.update(shape="rectangle", height="0.3", fontname="arial", fontsize="10")
        g.edge_attr.update(constraint="true", arrowhead="onormal")

        visitor = GraphvizFileTreeVisitor(self.start, g)
        Files.walk_file_tree(self.start, visitor)

        return g

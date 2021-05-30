from io import StringIO
import os.path
from pathlib import Path
from . import filevisitor


class TraceFileTreeVisitor(filevisitor.FileVisitor):

    def __init__(self, starting_dir: Path, buffer: StringIO):
        self.start = starting_dir
        self.buffer = buffer

    def pre_visit_directory(self, directory: Path) -> filevisitor.FileVisitResult:
        relative_path = os.path.relpath(directory, self.start)
        self.buffer.write("> {}/\n".format(relative_path))
        return filevisitor.FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, io_error: IOError) -> filevisitor.FileVisitResult:
        relative_path = os.path.relpath(directory, self.start)
        self.buffer.write("< {}/\n".format(relative_path))
        return filevisitor.FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> filevisitor.FileVisitResult:
        relative_path = os.path.relpath(file, self.start)
        self.buffer.write("= {}\n".format(relative_path))
        return filevisitor.FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, io_error: IOError) -> filevisitor.FileVisitResult:
        relative_path = os.path.relpath(file, self.start)
        self.buffer.write("! {}\n".format(relative_path))
        return filevisitor.FileVisitResult.CONTINUE


class TraceMain:

    def __init__(self, starting_dir: Path, excludes=[]):
        self.start = starting_dir
        self.buffer = StringIO()
        self.excludes = excludes

    def trace(self):
        visitor = TraceFileTreeVisitor(self.start, self.buffer)
        filevisitor.Files.walk_file_tree(visitor, self.start, self.excludes)
        result = self.buffer.getvalue()
        self.buffer.close()
        return result


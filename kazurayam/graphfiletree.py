import os.path
from pathlib import Path
from filevisitor import FileVisitor, FileVisitResult


class GraphFileTreeVisitor(FileVisitor):

    def __init__(self, starting_dir: Path):
        self.base = starting_dir

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        relative_path = os.path.relpath(directory, self.base)
        print("> {}/".format(relative_path))
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, io_error: IOError) -> FileVisitResult:
        relative_path = os.path.relpath(directory, self.base)
        print("< {}/".format(relative_path))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        relative_path = os.path.relpath(file, self.base)
        print("= {}".format(relative_path))
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, io_error: IOError) -> FileVisitResult:
        relative_path = os.path.relpath(file, self.base)
        print("! {}".format(relative_path))
        return FileVisitResult.CONTINUE

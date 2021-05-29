from pathlib import Path
from filevisitor import FileVisitor, FileVisitResult


class TreeListingVisitor(FileVisitor):

    def __init__(self):
        pass

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        print("> {}/".format(directory))
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path, ioerror: IOError) -> FileVisitResult:
        print("< {}/".format(directory))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        print("= {}".format(file))
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, ioerror: IOError) -> FileVisitResult:
        print("! {}".format(file))
        return FileVisitResult.CONTINUE

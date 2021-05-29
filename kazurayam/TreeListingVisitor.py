from pathlib import Path
from kazurayam.filevisitor import FileVisitor, FileVisitResult, FileTreatmentException


class TreeListingVisitor(FileVisitor):

    def __init__(self):
        pass

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        print("> {}/".format(directory))
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path) -> FileVisitResult:
        print("< {}/".format(directory))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        print("= {}".format(file))
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, exception: FileTreatmentException) -> FileVisitResult:
        print("! {}".format(file))
        return FileVisitResult.CONTINUE



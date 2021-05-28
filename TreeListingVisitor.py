from pathlib import Path
from filevisitor import Files, FileVisitor, FileVisitResult, FileTreatmentException


class TreeListingVisitor(FileVisitor):

    def __init__(self):
        pass

    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        print("pre_visit_directory {}".format(directory))
        return FileVisitResult.CONTINUE

    def post_visit_directory(self, directory: Path) -> FileVisitResult:
        print("post_visit_directory {}".format(directory))
        return FileVisitResult.CONTINUE

    def visit_file(self, file: Path) -> FileVisitResult:
        print("visit_file {}".format(file))
        return FileVisitResult.CONTINUE

    def visit_file_failed(self, file: Path, exception: FileTreatmentException) -> FileVisitResult:
        print("visit_file_failed {}".format(file))
        return FileVisitResult.CONTINUE


if __name__ == '__main__':
    starting_dir = Path("./tmp")
    file_to_search = "greeting"
    crawler = TreeListingVisitor()
    Files.walk_file_tree(starting_dir, crawler)

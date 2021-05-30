from abc import ABCMeta, abstractmethod
from pathlib import Path
from enum import IntEnum, auto


class FileVisitResult(IntEnum):
    CONTINUE = auto()
    SKIP_SIBLINGS = auto()
    SKIP_SUBTREE = auto()
    TERMINATE = auto()


class FileVisitor(metaclass=ABCMeta):
    """
    An homage to java.nio.file.FileVisitor
    """

    @abstractmethod
    def pre_visit_directory(self, directory: Path) -> FileVisitResult:
        pass

    @abstractmethod
    def post_visit_directory(self, directory: Path, io_error: IOError) -> FileVisitResult:
        pass

    @abstractmethod
    def visit_file(self, file: Path) -> FileVisitResult:
        pass

    @abstractmethod
    def visit_file_failed(self, file: Path, io_error: IOError) -> FileVisitResult:
        pass


class Files:
    @staticmethod
    def walk_file_tree(p: Path, visitor: FileVisitor):
        """
        :param p: Path
        :param visitor: FileVisitor
        :return: void
        """
        if p.is_dir():
            visitor.pre_visit_directory(p)
            for entry in p.iterdir():
                Files.walk_file_tree(entry, visitor)
            visitor.post_visit_directory(p, None)
        else:
            visitor.visit_file(p)

from abc import ABCMeta, abstractmethod
from pathlib import Path
from enum import IntEnum, auto


class FileTreatmentException(Exception):
    pass


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
    def post_visit_directory(self, directory: Path) -> FileVisitResult:
        pass

    @abstractmethod
    def visit_file(self, file: Path) -> FileVisitResult:
        pass

    @abstractmethod
    def visit_file_failed(self, file: Path, exception: FileTreatmentException) -> FileVisitResult:
        pass


class Files:
    @staticmethod
    def walk_file_tree(p: Path, crawler: FileVisitor):
        """
        :param p: Path
        :param crawler: FileVisitor
        :return: void
        """
        if p.is_dir():
            crawler.pre_visit_directory(p)
            for entry in p.iterdir():
                Files.walk_file_tree(entry, crawler)
            crawler.post_visit_directory(p)
        else:
            crawler.visit_file(p)

from pathlib import Path
from filevisitor import Files
from tracefiletree import TraceFileTreeVisitor

if __name__ == '__main__':
    starting_dir = Path(".")
    crawler = TraceFileTreeVisitor(starting_dir)
    Files.walk_file_tree(starting_dir, crawler)

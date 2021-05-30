"""
kazurayam/demo.py
"""
from pathlib import Path
from filevisitor import Files
from tracefiletree import TraceFileTreeVisitor

if __name__ == '__main__':
    starting_dir = Path(".")
    visitor = TraceFileTreeVisitor(starting_dir)
    Files.walk_file_tree(visitor, starting_dir)

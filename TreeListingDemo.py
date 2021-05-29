from pathlib import Path
from kazurayam.filevisitor import Files
from kazurayam.TreeListingVisitor import TreeListingVisitor

if __name__ == '__main__':
    starting_dir = Path("./kazurayam")
    crawler = TreeListingVisitor()
    Files.walk_file_tree(starting_dir, crawler)

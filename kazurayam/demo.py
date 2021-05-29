from pathlib import Path
from filevisitor import Files
from treelisting import TreeListingVisitor

if __name__ == '__main__':
    starting_dir = Path("")
    crawler = TreeListingVisitor()
    Files.walk_file_tree(starting_dir, crawler)

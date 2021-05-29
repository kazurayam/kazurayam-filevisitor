from setuptools import setup, find_packages

setup(
    name="kazurayam-filevisitor",
    version="0.1.0",
    description="FileVisitor in Python, with a usage sample that draws file tree graph by Graphviz",
    author="kazurayam",
    author_email="kazuaki.urayama@gmail.com",
    url="https://github.com/kazurayam/kazurayam-filevisitor",
    include_package_data=True,
    zip_safe=False,
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points="""
      [console_scripts]
      treelisting = kazurayam:TreeListingVisitor 
    """,
)
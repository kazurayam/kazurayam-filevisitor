import os
import pytest
from fileutils import init_dir


@pytest.fixture(scope='session')
def basedir():
    project_dir = os.getcwd()
    base = os.path.join(project_dir, "./tmp")
    init_dir(base)
    yield base
    os.chdir(project_dir)

import os
import pytest
from kazurayam.fileutils import init_dir, write_file


@pytest.fixture(scope='module')
def basedir():
    project_dir = os.getcwd()
    base = os.path.join(project_dir, "../tmp")
    init_dir(base)
    yield base
    os.chdir(project_dir)


def test_main(basedir):
    print("\ntest_main starting")
    wt = os.path.join(basedir, 'test_main')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)


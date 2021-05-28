import os
import pytest
import shutil
import pathlib


@pytest.fixture(scope='module')
def basedir():
    project_dir = os.getcwd()
    base = os.path.join(project_dir, "tmp")
    init_dir(base)
    yield base
    os.chdir(project_dir)


def init_dir(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)


def write_file(wt, path, text):
    f = pathlib.Path(os.path.join(wt, path))
    os.makedirs(f.parent, exist_ok=True)
    with open(os.path.join(wt, path), 'w') as file:
        file.write(text)
    return f


def test_main(basedir):
    wt = os.path.join(basedir, 'test_main')
    init_dir(wt)
    os.chdir(wt)
    f = write_file(wt, 'src/greeting', 'Hello, world!\n')
    assert os.path.exists(f)


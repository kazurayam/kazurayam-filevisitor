import os
import pathlib
import shutil

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


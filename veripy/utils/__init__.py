from contextlib import contextmanager
import os


def mkdir(dir):
    """
    Checks if directory exists, if not make a directory, given the directory path
    :param: <string>dir: Full path of directory to create
    """
    if not os.path.exists(dir):
        os.makedirs(dir)


@contextmanager
def open_and_purge(name, mode='r'):
    """ Similar to the built-in open() call. This context manager opens a file
    in the specified mode. The only difference is that this function deletes the
    file once the context manager exits.
    """
    f = open(name, mode)
    yield f
    f.close()
    os.remove(name)

from contextlib import contextmanager
import os
import time


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


def allow_retries(retry_on=[], wait=time.sleep, retries=3, delay=2):
    """ A general purpose decorator that allows a given function to be retried
    after certain failures.

    **Example**

    Suppose we have a function that occasionally throws errors if it doesn't get
    its way. In that case we can allow the function to be tried if a certain set
    of critera are met. In this case, if the exception thrown matches any of the
    exceptions in the `retry_on` parameter, then the function will be retried
    after a delay.

    The delay is a linear backoff that attempts to retry the function after greater
    and greater delays until the maximum retry limit is reached. Once the limit
    is reached, the latest exception is rethrown to allow other aspects of the
    code to catch the errors and respond.

    By default the delay method is just `time.sleep` but any function that takes
    a seconds parameter can be supplied. To ignore the delay and retry immediately
    either set the delay to 0 or the wait function to None.

    ::

        # Retry when the function throws a tantrum.

        @allow_retries(retry_on=(ThrowATantrum,), retries=2)
        def touchy_function(*args, **kwargs):
            if sometimes:
                raise ThrowATantrum()
            else:
                do_work()

        # -----

        # Retry *immediately* after the function throws a tantrum.

        @allow_retries(retry_on=(ThrowATantrum,), retries=2, wait=None)
        def touchy_function(*args, **kwargs):
            if sometimes:
                raise ThrowATantrum()
            else:
                do_work()

    """
    def wrapper(func):
        def func_wrapper(*args, _depth=1, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if not any(isinstance(e, e_type) for e_type in retry_on):
                    # The exception encountered was not supposed to trigger
                    # a retry. Something else has occurred.
                    raise e
                elif retries < _depth:
                    # We've retried as many times as we can.
                    raise e

            # Attempt a retry of the function after a delay if any.
            if wait:
                wait(delay * _depth)
            return func_wrapper(*args, _depth=_depth+1, **kwargs)
        return func_wrapper
    return wrapper

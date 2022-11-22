import time

def executiontime(func) -> None:
    """A decorator that prints time taken by function `func` 
    Params::
        func (def): The function executed
    Usage::
    >>> from PythonicBrain.PBDecorator import executiontime
    >>> @executiontime
    >>> def hello():
    >>>    ...
    """
    def _func(*args, **kwargs):
        start = time.time()
        fn = func(*args, **kwargs)
        end = time.time()
        print(f"INFO: Time of Execution: {end-start}")
        return fn
    return _func
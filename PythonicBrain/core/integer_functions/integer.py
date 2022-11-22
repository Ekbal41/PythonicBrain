def float_range(start, stop, step):
    r"""returns a iter with given float value
    Returns a float range, compare it to python built in 
    range with float type
    Usage::
        float_range(1.1,2.9,.1)
    """
    while start < stop:
        yield float(start)
        start += step
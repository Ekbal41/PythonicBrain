from collections import defaultdict

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
        
#-------------------------------------------------------

def groupby_count(i, key=None, force_keys=None):
    """Group a list of elements as per the count
    Usage::
        >>> from PythonivBrain.PBIntrger import groupby
        >>> print(groupby_count([1,1,1,2,3]))
        [(1,3),(2,1),(3,1)]
    """
    counter = defaultdict(lambda: 0)
    if not key:
        def key(o): return o

    for k in i:
        counter[key(k)] += 1

    if force_keys:
        for k in force_keys:
            counter[k] += 0

    return counter.items()

#------------------------------------------------------
def chunks(lst, n):
    """Yield successive n-sized chunks from lst.
    
    Usage::
        >>> from PythonivBrain.PBIntrger import chunk
        >>> li=[1,3,5,6,8]
        >>> for g in chunks(li,2):
        ...     print(g)
    """
    for i in range(0, len(lst), n):
        yield lst[i:i + n]
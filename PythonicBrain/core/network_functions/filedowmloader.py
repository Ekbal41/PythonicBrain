import os
import sys
from urllib.request import urlopen,Request
import requests




def download_file(url, path,overwrite=False):
    """Downloads a file from `url` and saves it to the given `path`
    Usage::
        >>> from PythonicBrain.PBNetwork import download_file
        >>> download_file('https://www.somewebsite.com/somephoto.jpg','./images',True)
    """
    file_name = os.path.basename(url)
    if not overwrite and os.path.exists(file_name):
        raise Exception("Target file already exists")
    request_site = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    u = urlopen(request_site)
    
    target = file_name
    if path:
        target = os.path.join(path,target)
    f = open(target+".temp", 'wb')
    meta = u.info()
    file_size = int(meta.get("Content-Length")[0])
    print("Downloading: %s Bytes: %s" % (file_name, file_size))
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (
            file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        sys.stdout.write(status)
        if not '100.00' in status:
            sys.stdout.write('\r')
    f.close()
    if overwrite:
        if os.path.exists(target):
            os.remove(target)
    os.rename(target+".temp", target)
    return 
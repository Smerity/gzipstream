# gzipstream

`gzipstream` allows Python to process multi-part gzip files from a streaming source.
The library is originally intended for use with the Python [warc library](http://warc.readthedocs.org/en/latest/) for processing [Common Crawl](http://commoncrawl.org/) and other web archive data.

# Installation

If you are using pip, simply run the command `pip install -e git+https://github.com/commoncrawl/gzipstream.git#egg=gzipstream`.
You can also install using `python setup.py install` if so desired.

# Usage

As an example of usage, `examples/streaming_commoncrawl_from_s3.py` shows how `gzipstream` can be used to incrementally process a gzipped web archive (WARC) file.
The file is almost a gigabyte in size, selected randomly from the 2014-15 Common Crawl dataset and hosted on Amazon S3.
Without `gzipstream`, processing of the file would only be possible by fully downloading it.
This is highly inefficient as (a) a gzipped WARC file is composed of multiple independent gzip files and (b) the WARC file is hunderds of megabytes in size.

For minimal usage however...

```python
from gzipstream import GzipStreamFile
f = open('huge_file.gz') # Any streaming file object that supports `read`
gz = GzipStreamFile(f)
```

# License

MIT License, as per `LICENSE`

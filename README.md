# gzipstream

`gzipstream` allows Python to process multi-part gzip files from a streaming source.
Primarily intended for use with the [warc library](http://warc.readthedocs.org/en/latest/) for processing [Common Crawl](http://commoncrawl.org/) and other web archive data.

As an example of usage, `examples / streaming_commoncrawl_from_s3.py` shows how `gzipstream` can be used with `boto` and `warc` to process a randomly selected gzip web archive (WARC) from the 2014-15 Common Crawl dataset.
Without `gzipstream`, processing of the file would only be possible by fully downloading it.
This is highly inefficient as (a) a gzipped WARC file is composed of multiple independent gzip files and (b) the WARC file is hunderds of megabytes in size.

# Usage

For detailed usage, see the examples folder, but minimally...

```python
from gzipstream import GzipStreamFile
f = open('huge_file.gz') # Any streaming file object that supports `read`
gz = GzipStreamFile(f)
```

# License

MIT License, as per `LICENSE`

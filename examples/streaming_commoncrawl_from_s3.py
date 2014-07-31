import boto
from boto.s3.key import Key
from gzipstream import GzipStreamFile
import warc

if __name__ == '__main__':
  # Let's use a random gzipped web archive (WARC) file from the 2014-15 Common Crawl dataset
  ## Connect to Amazon S3 using anonymous credentials
  conn = boto.connect_s3(anon=True)
  pds = conn.get_bucket('aws-publicdatasets')
  ## Start a connection to one of the WARC files
  k = Key(pds)
  k.key = 'common-crawl/crawl-data/CC-MAIN-2014-15/segments/1397609521512.15/warc/CC-MAIN-20140416005201-00000-ip-10-147-4-33.ec2.internal.warc.gz'

  # The warc library accepts file like objects, so let's use GzipStreamFile
  f = warc.WARCFile(fileobj=GzipStreamFile(k))
  for num, record in enumerate(f):
    if record['WARC-Type'] == 'response':
      # Imagine we're interested in the URL, the length of content, and any Content-Type strings in there
      print record['WARC-Target-URI'], record['Content-Length']
      print '\n'.join(x for x in record.payload.read().replace('\r', '').split('\n\n')[0].split('\n') if 'content-type:' in x.lower())
      print '=-=-' * 10
    if num > 100:
      break

import zlib


class GzipStreamFile(object):
  READ_SIZE = 1024 * 8

  def __init__(self, stream):
    self.stream = stream
    self.decoder = None
    self.restart_decoder()
    ###
    self.unused_buffer = ''
    self.finished = False

  def restart_decoder(self):
    unused_raw = self.decoder.unused_data if self.decoder else None
    self.decoder = zlib.decompressobj(16 + zlib.MAX_WBITS)
    if unused_raw:
      self.unused_buffer += self.decoder.decompress(unused_raw)

  def read(self, size):
    # Check if we need to start a new decoder
    if self.decoder and self.decoder.unused_data:
      self.restart_decoder()
    # Use unused data first
    if len(self.unused_buffer) > size:
      part = self.unused_buffer[:size]
      self.unused_buffer = self.unused_buffer[size:]
      return part
    # If the stream is finished and no unused raw data, return what we have
    if self.stream.closed or self.finished:
      self.finished = True
      buf, self.unused_buffer = self.unused_buffer, ''
      return buf
    # Otherwise consume new data
    raw = self.stream.read(GzipStreamFile.READ_SIZE)
    if len(raw):
      self.unused_buffer += self.decoder.decompress(raw)
    else:
      self.finished = True
    return self.read(size)

  def readline(self):
    chars = []
    c = self.read(1)
    while c != '\n':
      chars.append(c)
      c = self.read(1)
    chars.append(c)
    line = ''.join(chars)
    return line

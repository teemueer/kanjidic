import codecs

def read_lines(filepath, encoding='euc-jp'):
    with codecs.open(filepath, 'r', encoding) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'): continue
            yield line


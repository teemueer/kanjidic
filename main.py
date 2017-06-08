import re
from func import read_lines

segment_pattern = re.compile(r'[^ {]+|{.*?}', re.UNICODE)

for line in read_lines('kanjidic'):
    fields = segment_pattern.findall(line)
    print fields
    break

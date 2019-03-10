import os
statinfo = os.stat('Test.rtf')
print(statinfo.st_size)
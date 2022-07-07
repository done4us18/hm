import marshal
e= marshal.loads('c\x00\x00\x00\x00\x00\x00\x0')

from uncompyle6.main import decompile as Xenzi
Xenzi(2.7,e,open('umbrella.py','w'))

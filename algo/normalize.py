#!/usr/bin/env python

import os
import pdb
import re
from cucco import Cucco

cucco = Cucco()
normalizations = [
	('replace_punctuation', {'replacement': ' '}),
	'remove_extra_white_spaces'
	]

filename = 'cbt_data/data/cbt_train.txt'
fout = open('cbt_data/input.txt', 'w')
fin = open(filename, 'r')
text = fin.read()
text = re.sub('LCB.*?RCB', '', text, flags=re.DOTALL)
text = re.sub('LRB.*?RRB', '', text, flags=re.DOTALL)
text.decode('utf-8')
for line in text.split('\n'):
	try:
		fout.write(cucco.normalize(line, normalizations))
		fout.write(' ')
	except:
		continue

fout.close()

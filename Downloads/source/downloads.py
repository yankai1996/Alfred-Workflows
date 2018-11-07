# -*- coding: utf-8 -*-
import os 
import sys
from AlfredItemsList import *

home_path = os.path.expanduser("~")
dir_path = os.path.join(home_path, 'Downloads')

items = []
for filename in os.listdir(dir_path):
	if len(sys.argv) > 1:
		if sys.argv[1].lower() not in filename.lower():
			continue
	if filename.startswith('.') or filename.startswith('$'):
		continue
	file_path = os.path.join(dir_path, filename)
	items.append((os.stat(file_path).st_birthtime, filename))

items.sort(key=lambda x: x[0], reverse=True)

al = AlfredItemsList(fileicon=True)
for item in items:
	filename = item[1].decode('utf-8')
	file_path = os.path.join(dir_path, filename)
	al.append(file_path, filename, 'Press ENTER to open...', file_path)

print al
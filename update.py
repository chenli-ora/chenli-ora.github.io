# This is my python script to update my website with jemdoc
import sys
import os
print(sys.version)
files = ['index', 'research', 'teaching', 'activities', 'talk_list']

for i in files:
	os.system('python jemdoc.py '+i)

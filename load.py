#import time
#
#load = '_'
#count = 0
#
#for x in range(21):
#     time.sleep(0.3)
#     print(f'\rLoading {x}% [{load}]', end='', flush=True)
#     count += 1
#     if count == 3:



#	 load += '_'
#print('\nDone')

import time

load = '_'
count = 0

for t in range(21):
	time.sleep(0.3)
	print(f'\rLoading {t}% [{load}]', end='', flush=True)
	count += 1
	if count == 3:
		count = 0
		load += '_'
print('\nDone')

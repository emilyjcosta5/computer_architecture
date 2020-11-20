import random

def generate_1():
	'''
	Assume that you have a direct-mapped 16KB instruction cache with a (32B block size).
	Generate an address stream that will touch every cache line once, but no more than
	once.
	0 < ADDRESS < ff,ff,ff,ff - last two used for offset 
	'''
	# in bytes
	i_cache_size 	= 16384
	block_size 		= 32
	no_addresses 	= i_cache_size/block_size
	addresses 		= []
	i 				= 0

	while(i < no_addresses):
		label 		= 2
		cache_line 	= bin(i).split('b')[-1]
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(cache_line + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))
		i = i+1
	#print(addresses)
	with open('trace_1.txt', 'w') as f:
		for address in addresses:
			f.write('%s\n'%address)

if __name__=='__main__':
	generate_1()
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

def generate_2():
	'''
	Assume the same instruction cache organization as in (1), but now the instruction cache
	is 2-way set associative, with LRU replacement. The total cache space is still 16KB with
	a 32B block size, but now you have 1/2 the number of indices. Generate an address
	stream that touches every cache index only 7 times, producing 3 misses and 4 hits, but
	only accesses 3 unique addresses per index.
	'''
	i_cache_size 	= 16384
	block_size 		= 32
	n_way_set		= 2
	no_unique		= 3
	no_addresses 	= (i_cache_size/block_size)/n_way_set
	addresses 		= []
	i 				= 0

	while(i < no_addresses):
		# miss
		label 		= 2
		tag		 	= bin(i*no_unique).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# miss
		label 		= 2
		tag		 	= bin(i*no_unique+1).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# miss
		label 		= 2
		tag			= bin(i*no_unique+2).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		i = i+1

	#print(addresses)
	with open('trace_2.txt', 'w') as f:
		for address in addresses:
			f.write('%s\n'%address)

def generate_3():
	'''
	Repeat part 2, but now produce 5 misses and 5 hits, again with only 3 unique address per
	index, but produce an interleaving pattern of Miss-Hit-Miss-Hit-Miss-Hit-…….
	'''
	i_cache_size 	= 16384
	block_size 		= 32
	n_way_set		= 2
	no_unique		= 3
	no_addresses 	= (i_cache_size/block_size)/n_way_set
	addresses 		= []
	i 				= 0

	while(i < no_addresses):
		# miss
		label 		= 2
		tag		 	= bin(i*no_unique).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address0	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address0))

		# hit
		addresses.append('%d %s'%(label, address0))

		# miss
		label 		= 2
		tag		 	= bin(i*no_unique+1).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address1 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address1))

		# hit
		addresses.append('%d %s'%(label, address1))

		# miss
		label 		= 2
		tag			= bin(i*no_unique+2).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address2 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address2))

		# hit
		addresses.append('%d %s'%(label, address2))

		# miss
		addresses.append('%d %s'%(label, address0))

		# hit
		addresses.append('%d %s'%(label, address0))

		# miss
		addresses.append('%d %s'%(label, address1))

		# hit
		addresses.append('%d %s'%(label, address1))

		i = i+1

	#print(addresses)
	with open('trace_3.txt', 'w') as f:
		for address in addresses:
			f.write('%s\n'%address)

def generate_4():
	'''
	Assume that you have a 4-way set associate 32KB data cache with a (32B block size).
	Generate an address stream that will generate 6 hits and 4 misses. Make sure that your
	stream includes both loads and stores.
	'''
	i_cache_size 	= 16384
	block_size 		= 32
	n_way_set		= 4
	no_unique		= 3
	no_addresses 	= (i_cache_size/block_size)/n_way_set
	addresses 		= []
	i 				= 0

	while(i < no_addresses):
		# miss
		label 		= 2
		tag		 	= bin(i*no_unique).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# miss
		label 		= 2
		tag		 	= bin(i*no_unique+1).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# miss
		label 		= 2
		tag			= bin(i*no_unique+2).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# miss
		label 		= 2
		tag			= bin(i*no_unique+3).split('b')[-1]
		index 		= format(i, '08b')
		offset 		= format(random.randint(0,31), '05b')
		address 	= hex(int(tag + index + offset, 2)).split('x')[-1]
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		# hit
		addresses.append('%d %s'%(label, address))

		i = i+1

	#print(addresses)
	with open('trace_4.txt', 'w') as f:
		for address in addresses:
			f.write('%s\n'%address)

if __name__=='__main__':
	generate_3()
	generate_4()
import numpy as np

n = 20
nr_rows = n+1
V = nr_rows*nr_rows
array =  np.zeros((V,), dtype=int)
print(array)

col = n-1
row = n
array[V-1] = 1
print(array)

diagonal_len = 2
start_to_decrement = False
k = 0
while k < 2*nr_rows - 1:
	diagonal_counter = 1
	#print("row: ", row)
	#print("col: ", col)
	print("diagonal_len: ", diagonal_len)
	while diagonal_counter <= diagonal_len:
		if diagonal_counter == diagonal_len:
			cur_index = col + row*nr_rows
			# processa adjacentes
			if col == n:
				right = 0
			else:
				right = array[cur_index+1]
			if row == n:
				down = 0
			else:
				down = array[cur_index+n+1]
			
			array[cur_index] = down + right
			diagonal_counter += 1
			if start_to_decrement == False and diagonal_len != (n+1):
				row = n
				col = nr_rows - diagonal_len - 1
			elif start_to_decrement == False:
				col = 0
				row = n-1
			elif start_to_decrement == True:
				col = 0
				row = diagonal_len - 2

			print("col: ", col)
		else:
			cur_index = col + row*nr_rows
			# processa adjacentes
			if col == n:
				right = 0
			else:
				right = array[cur_index+1]
			if row == n:
				down = 0
			else:
				down = array[cur_index+n+1]
			
			array[cur_index] = down + right
			diagonal_counter += 1
			row = row - 1
			col = col + 1

	if start_to_decrement == False and diagonal_len == (n+1):
		start_to_decrement = True
	if start_to_decrement == False:
		diagonal_len += 1
	else:
		diagonal_len -= 1
	k += 1

print(array)



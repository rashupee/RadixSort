# Radix Algorithm Sort of list of integers

#	Using the LSF (Least significant figure) First (From the right)
#		(as opposed to MSF)




# [170, 45, 75, 90, 2, 802, 2, 66]

# [{170, 90}, {2, 802, 2}, {45, 75}, {66}]

# [{02, 802, 02}, {45}, {66}, {170, 75}, {90}]

# [{002, 002, 045, 066, 075, 090}, {170}, {802}]

# I could pre-prepare a list of strings of the integers where each string has a length matching the largest
# 	integer in the list
# Requires a pass through the original array to find the largest integer.

def length_of_max_element(array):
	max_length = 0
	for element in array:
		if len(element) > max_length:
			max_length = len(element)

	return max_length
	


def stringify_list(original_array):
	# Transforms list of integers into list of strings
	list_of_strings = [str(integer) for integer in original_array]

	return list_of_strings



def prepend_zeroes(max_length, string_array):
	# Returns list of strings where elements are adjusted to have enough prepended zeroes so that they
	#	all have the same length as max_length
	working_array = []
	for element in string_array:
		working_array.append( (max_length-len(element))*'0' + element )

	return working_array



def flattened_2D_array(array_2D):
	# Flattens an array to one less dimension
	flattend_array = []
	for array in array_2D:
		for element in array:
			flattend_array.append(element)

	return flattend_array




def bucket_list(key_position,array):
	# Returns a transformation on a given array with one iteration of organizing based on given key_position
	# In particular, a list of lists is returned where every sublist is a bucket where every element will 
	# 	have the same value at the key_position



	return None










def LSF_sorter(original_array):
	# Returns a radix sorted array of the integers in the supplied array
	# LSF is a Stable sort
	# This function will not change the original_array

	# This function orchestrates transformations and measures done by methods above to achieve the sort transformation

	string_list = stringify_list(original_array)
	max_length = length_of_max_element(string_list)
	working_array = prepend_zeroes(max_length, string_list)

	# Now I have a good starting point to actually radix sort
	# First idea is to iterate the key_position from zero to max_length-1 and bucket sort from the right.

	# I think I am going to flatten or linearize lists of lists...



	return None
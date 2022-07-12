# Radix Algorithm Sort of list of integers

#	Using the LSF (Least significant figure) First (From the right)
#		(as opposed to MSF)


def length_of_max_element(array):
	# Returns the length of longest string
	# Expects array of strings
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
	#	all have the length max_length
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




def radix_sort(working_array):
	# Returns a transformation of the non-empty working_array which is a radix sorted list of strings

	# Iterate over the length of the number strings, starting at the LSF (right side digit):
	#	Each iteration:
	#		do the bucket sort according to the key_strings which are single character strings
	#			of the digits
	#		Then flatten array into a new working array


	# Create list of key strings
	key_strings = [str(index) for index in range(0,10)]

	length_of_strings = len(working_array[0]) # They are all the same by construction

	for key_position in range( length_of_strings-1, -1, -1 ):

		# Initialize empty buckets-- separate bucket for each key_string
		buckets = [ [] for symbol in key_strings]

		# Populate the buckets
		for i in range(0, len(buckets) ):
			for element in working_array:
				if element[key_position] == key_strings[i]:
					buckets[i].append(element)

		# Update the working_array
		working_array = flattened_2D_array(buckets)

	return working_array



def back_to_integers(array):
	# Expects a list of string versions of integers
	# Returns list of integers

	return [ int(element) for element in array ]





def LSF_radix_sort(original_array):
	# Returns a radix sorted array of the integers in the supplied array
	# LSF is a Stable sort
	# This function will not change the original_array

	# This function orchestrates transformations and measures done by methods above to achieve the sort transformation

	string_list = stringify_list(original_array)
	max_length = length_of_max_element(string_list)
	working_array = prepend_zeroes(max_length, string_list)
	answer = back_to_integers(radix_sort(working_array))

	# Now I have a good starting point to actually radix sort
	# First idea is to iterate the key_position from zero to max_length-1 and bucket sort from the right

	return answer
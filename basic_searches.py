"""
Basic Search Algorithms implemented in different ways as functions.
Each function returns True if found and False if not found.
Also has a basic functions to allow repeated call for user input.
"""

"""
Binary Search
	Splits the list in half recursively until requested value is found or their is one item left.
	Note: This requires the list input to be ordered. 
"""

#Uses recurssion to recursively split the list in half.
def binary_search_one(lst, value):
	length = len(lst)
	half = length // 2
	if lst[half] == value:
		return True
	elif length == 1:
		return False
	elif lst[half] > value:
		del lst[-half:]
		return binary_search_one(lst, value)
	elif lst[half] < value:
		del lst[:half]
		return binary_search_one(lst, value)

#Uses a while loop to recursively split the list in half.
def binary_search_two(lst, value):
	while True:
		length = len(lst)
		half = length // 2
		if lst[half] == value:
			return True
		elif length == 1:
			return False
		elif lst[half] > value:
			del lst[-half:]
		elif lst[half] < value:
			del lst[:half]

"""
Linear Search
	Searches through each individual element one by one, to compare if this is the requested value.
"""

#Uses a for loop to loop through all items in the list.
def linear_search_one(lst, value):
	for val in lst:
		if val == value:
			return True
	return False

#Uses a for loop to loop through each index in the list.
def linear_search_two(lst, value):
	for i in range(len(lst)):
		if lst[i] == value:
			return True
	return False

#Uses a while to loop through each index within the list.
def linear_search_three(lst, value):
	i = 0
	while i < len(lst):
		if lst[i] ==  value:
			return True
		i += 1
	return False

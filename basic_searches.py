"""
Basic Search Algorithms implemented in different ways as functions.
"""

#Creates a list of user input, breaks when user enters nothing.
def get_list():
	lst = []
	print("To finish the list, please input nothing and press enter.")
	while True:
		new_item = input("Please enter a new item: ")
		if new_item == "":
			break
		lst.append(new_item)
	return lst

"""
Linear Search
	Searches through each individual element one by one, to compare if this is the requested value.
	Each function returns True if found and False if not found.
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

"""
Binary Search
	Splits the list in half recursively until requested value is found or their is one item left.
	Note: This requires the list to be ordered. 
	Each function returns True if found and False if not found.
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

#Main program
lst = get_list()
print("\nYour list: ", lst)
value = input("Please eneter a value to search for: ")

print("\nLinear search one:", linear_search_one(lst, value))
print("Linear search two:", linear_search_two(lst, value))
print("Linear search three:", linear_search_three(lst, value))
print("\n--------------------------------------------------------")

print("\nPlease ensure the list is ordered.")
lst = get_list()
print("\nYour list: ", lst)
value = input("Please eneter a value to search for: ")

print("\nBinary search one:", binary_search_one(lst, value))
print("Binary search two:", binary_search_two(lst, value))
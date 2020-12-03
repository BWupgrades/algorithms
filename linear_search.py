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

lst = get_list()
print("\nYour list: ", lst)

value = input("Please eneter a value to search for: ")

print("\nSearch one:", (linear_search_one(lst, value)))
print("Search two:", (linear_search_two(lst, value)))
print("Search three:", (linear_search_three(lst, value)))
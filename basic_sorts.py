"""
Basic Sort Algorithms implemented in different ways as functions.
Each function returns the sorted list.
Also has some basic functions to allow for user input or validation.
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

#Splits list input into 2 lists of integers and strings.
def split_list(lst):
	int_lst, str_lst = [], []
	for item in lst:
		try:
			int(item)
			int_lst.append(item)
		except:
			str_lst.append(item)
	return int_lst, str_lst

#Merges two given lists, used to merge integer and string list.
def merge_list(lst1, lst2):
	if lst1 and lst2:
		return lst1 + lst2
	elif lst1:
		return lst1
	elif lst2:
		return lst2
	return []

"""
Bubble Sort
	Loops through the list comparing adjecent values and swapping them until last 2 values compared.
	Repeates this process until no changes are made, each loop is called a pass.
"""

#Uses recurssion to complete each pass until no changes made.
def bubble_sort_one(lst):
	if len(lst):
		sorted = True
		for i in range(1, len(lst)):
			if lst[i-1] > lst[i]:
				lst[i-1], lst[i] = lst[i], lst[i-1]
				sorted = False
		if sorted:
			return lst
		return bubble_sort_one(lst)
	return []

#Uses a while loop to complete each pass until no changes made.
def bubble_sort_two(lst):
	if len(lst):
		while True:
			sorted = True
			for i in range(1, len(lst)):
				if lst[i-1] > lst[i]:
					lst[i-1], lst[i] = lst[i], lst[i-1]
					sorted = False
			if sorted:
				return lst
	return []

"""
Merge Sort
	Recursively splits the list until each element is on its own.
	Then Merges sub-lists together until all are merged and the complete list is sorted.
"""

"""
Quick Sort
	Selects a pivot point and loops through the list assigngs values to < or > sub-lists.
	Repeates this process until sub-lists contain one element, then the sorted list is created.
"""

"""
Insertion Sort
	Creates a 'sorted' list containing one element from the unsorted list.
	Loops through unsorted list, positioning each element in the sorted list in order.
"""

#Uses embeded for loop to compare values from both lists
def insertion_sort_one(lst):
	if len(lst):
		sorted_lst = []
		sorted_lst.append(lst[0])
		lst.pop(0)
		for i in range(len(lst)):
			placed = False
			for j in range(len(sorted_lst)):
				if sorted_lst[j] > lst[i]:
					sorted_lst.insert(j, lst[i])
					placed = True
					break
			if not placed:
				sorted_lst.append(lst[i])
		return sorted_lst
	return []

#Main program
lst = get_list()
print("\nYour list: ", lst)
int_lst, str_lst = split_list(lst)

print("\n--------------------------------------------------------")
print("\nBubble sort one:",  merge_list(bubble_sort_one(int_lst), bubble_sort_one(str_lst)))
print("Bubble sort two:",   merge_list(bubble_sort_two(int_lst), bubble_sort_two(str_lst)))

print("\n--------------------------------------------------------")
print("\nInsertion sort one:",  merge_list(insertion_sort_one(int_lst), insertion_sort_one(str_lst)))

print("\n--------------------------------------------------------")

"""
Basic Sort Algorithms implemented in different ways as functions.
Each function returns the sorted list.
Also has a basic functions to allow repated call for user input.
"""

#Creates a list of user input, breaks when user enters nothing.
def input_list():
	int_lst, str_lst = [], []
	print("To finish the list, please input nothing and press enter.")
	while True:
		new_item = input("Please enter a new item: ")
		if new_item == "":
			break
		try:
			int_lst.append(int(new_item))
		except:
			str_lst.append(new_item)
	return int_lst, str_lst

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
			try:
				if lst[i-1] > lst[i]:
					lst[i-1], lst[i] = lst[i], lst[i-1]
					sorted = False
			except:
				if str(lst[i-1]) > str(lst[i]):
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
				try:
					if lst[i-1] > lst[i]:
						lst[i-1], lst[i] = lst[i], lst[i-1]
						sorted = False
				except:
					if str(lst[i-1]) > str(lst[i]):
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
				try:
					if sorted_lst[j] > lst[i]:
						sorted_lst.insert(j, lst[i])
						placed = True
						break
				except:
					if str(sorted_lst[j]) > str(lst[i]):
						sorted_lst.insert(j, lst[i])
						placed = True
						break
			if not placed:
				sorted_lst.append(lst[i])
		return sorted_lst
	return []

#Main program
int_lst, str_lst = input_list()
print("\nYour list: ", int_lst + str_lst)

print("\n--------------------------------------------------------")
print("\nBubble sort one:", (bubble_sort_one(int_lst) + bubble_sort_one(str_lst)))
print("Bubble sort two:", (bubble_sort_two(int_lst) + bubble_sort_two(str_lst)))

print("\n--------------------------------------------------------")
print("\nInsertion sort one:", (insertion_sort_one(int_lst) + insertion_sort_one(str_lst)))

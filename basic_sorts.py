"""
Basic Sort Algorithms implemented in different ways as functions.
Each function returns the sorted list
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
Bubble Sort
	Loops through the list comparing adjecent values and swapping them until last 2 values compared.
	Repeates this process until no changes are made, each loop is called a pass.
"""

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

#Main program
lst = get_list()
print("\nYour list: ", lst)

print("\nInsertion sort one:",  insertion_sort_one(lst))
print("\n--------------------------------------------------------")

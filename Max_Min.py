def max_min(myarray):
	myarray.sort();
	min = myarray[0]
	max = myarray[-1]
	newarry = []
	newarry.append(min)
	newarry.append(max)
	return newarry
#output
print(max_min([78, 90, 10, 3, 56]))
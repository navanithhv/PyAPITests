# simple 'for' loop demonstration and its different angles

nav = ['ahah','123532567','klmn'];		# here a 'lst' is initilized
for n in nav:		# here how we declare a simple 'for' loop
	print n,len(n) ;		# it will print each values of list 'nav' and their length
	
	
# quite complex 'for' loop.

nav = ['ahah','123532567','klmn'];		# here a 'lst' is initilized
for n in nav[:]:		# here how we declare a simple 'for' loop and the slice symbol ':' can be used to modify the list sequence
	if len(n) > 5:		# check if any list element having length above 5
		nav.insert(0,n);# if above scenario exists then insert that element to 0th position of the list 'nav'
print nav;				# print all the elements of nav and it should display newly added element.


# here is the some example for 'range()' function.

nav = range(10);		# this function generates a list containing arithmetic progressions
print nav;				# this list will print 0  to 9 arithmatic numbers, keep in mind that it will generate list only upto 9 values, not 10

nith = range(5,10);
print nith;				# this list will print 5  to 9 arithmatic numbers, keep in mind that it will generate list upto 9 values, not 10


# we can use combination of 'len()' and 'range()' functions to itirate list in for loop

nav = ['ahah','123532567','klmn'];		# here a 'lst' is initilized
for n in range(len(nav)):	# here we are using range and len together to itirate 'nav' list and here 'n' will have index values of elements of 'nav' list.
	print n,nav[n];			# here 'n' will print index value of each element and 'nav[n]' will print element
	
	

# this is the demo for 'pass' statement

while True:
    pass  # This statement will be used when we need a statement syntactically but not for any action
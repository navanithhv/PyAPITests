#this sample script expalins some of the basics of python programming

a,b = 0,1;	#multiple assignment - a=0, b=1
while b<10:
	print b,	# This will display o/p in a line
	print b;	# This will display each o/p in new line
	a,b = b,a+b	#multiple assignment - a=b, b=a+b
	
# now we look in to some things about how to declare and call functions

def nav():				# this is very basic way of initiliziing function
	print "this is first line of the function";
	print " tihs is the second line";
	
nav()					# here we are calling function with function name and calling function name should be at below the function decleration, not at the above of decleration

#here we going little deeper to understand functions better


def nith(num1,num2):		# here we are passing 2 parameters
	print "adding num1 and num2 yields ->",(int(num1)+int(num2));	# here we need to convert the values from 'string' to 'int' to get proper o/p
	
a = raw_input("enter first value :");	# taking first input from console and defaulty it will be in 'string' form
b = raw_input("enter second value :");	# taking second input from console and defaulty it will be in 'string' form
	
nith(a,b)					# calling funtion and passing 2 values
	
# And now some things about converting and parsing data types

a = '5434'
print 'now a is string and its value is :',a;	# as said earlier now, by default, it is a string value
print ' float value of a is :',float(a);		# now we converted it to float
print ' int value of a is :',int(float(a));		# now we converted it to integer form
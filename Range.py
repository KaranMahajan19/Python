
print("Application to demonstration of range.")

# range(start,end,displacement)
		# start	:	by default 1
		# end 	:	No default value
		# displacement	:	by default 1

arr = range(1,5)
print(arr)

print("-----(1,5)-----")
for i in range(1,5):
	print(i)

print("-----1,5,1-----")
for i in range(0,5,1):
	print(i)

print("-----(1,10,2)-----")
for i in range(1,10,2):
	print(i+1)

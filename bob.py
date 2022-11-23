r = "bottles of beer"
q = r+" on the wall" 
a = q+","
b = q+"."
# Looping
for i in range(99, -2, -1):
	if (i > 2):
		print(i,a,i,r,".\nTake one down and pass it around,",i-1,b,"\n")
	elif(i == 1):
		print("2 bottles of beer on the wall, 2 bottles of beer.\nTake one down and pass it around, 1 bottle of beer on the wall.\n")	
	elif(i == 0):
		print("1 bottle of beer on the wall, 1 bottle of beer.\nTake one down and pass it around, no more bottles of beer on the wall.\n")	
	elif(i == -1):
		print("No more",a,"no more bottles of beer.\nGo to the store and buy some more, 99",b)
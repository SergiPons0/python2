def parells():
	l=[]
	for i in range(1,22,1):
    		if i %2 == 0:
        			l.append(i)
	return l
print(parells())

print([num for num in range(1,22,1) if num % 2 == 0])

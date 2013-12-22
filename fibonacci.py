#the sum of all the fibonacci numbers under 4 million.

f1 = 1;
f2 = 0;
f3 = 1;
sum = 0;

while f3 < 4000000:
	temp = f3 % 2;
	if temp == 0:
		sum = sum + f3;
	f2 = f3;
	f3 = f3 + f1;
	f1 = f2;

print " \n the sum is: ", sum 
		
	
	
		




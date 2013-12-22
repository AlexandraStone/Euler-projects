#difference in squares/.Problem #5 in Eulerproject

i = 1; 
all = 0;
x = 2;
sum = 1;

while i <= 100:

	square = i*i;
	all = all + square;
	i = i+1;

while x <= 100:
	
	sum = sum + x;
	x = x + 1;

Total = sum * sum;
difference = Total - all;

print " \n The difference is: ", difference



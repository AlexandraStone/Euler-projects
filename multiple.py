#this will compute the sum of all the multiples of 3 or 5 below 1000

count = 0;
total3 = 0;
total5 = 0;
total15 = 0;
x = 0;
y = 0;
z = 0;

while (count < 1000):
	x = count % 3;
	y = count % 5;
	z = count % 15;	

	if x == 0:
		total3 = total3 + count;
	if y == 0:
		total5 = total5 + count;
	if z == 0:
		total15 = total15 + count;
	count = count + 1;

print "\n The sum of all of the multiples of 3 under 1000 is: ", total3
print "\n The sum of all of the multiples of 5 under 1000 is: ", total5
print "\n The total sum: ", total3 + total5 - total15


 
	

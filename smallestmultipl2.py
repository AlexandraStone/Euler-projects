#smallest Multiple 

i = 30;
x = 2;
total = 0;

while total == 0:

	x = 2;

	while x <= 20:
	
		z = i % x;
		
		if z == 0:
			
			total = i;
			x = x + 1;

		if z != 0:
			
			x = 21;
			total = 0;
	else:
		i = i + 10;
		x = 2
else:
	print " \n smallest multiple of 1-20: ", total

#the largest prime factor


i = 2;
n = 0;

n = raw_input(" \n What number would you like to find the largest prime of: ");

while i * i < n:
    while n%i == 0:
        n = n / i
    i = i + 1


print " \n The largest prime is: ", n
	



			
				
			
				
				
					

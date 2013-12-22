#This Program is made to find the largest Plaidrome of 3 digit multipliers

#def reverse_int(p):
#	p2 = int(str(p)[::-1]);
#	return(p2)	

n = 100;
i = 100;
t = 0;


while (n <= 999):

	while(i <= 999):
	

		p = i * n;
		#print" \n value of p: ", p
		

		p2 = int(str(p)[::-1]);
		#print" \n value of p2: ", p2
	
		if (p2 == p and p2 > t): 
			t = p;
		
		i = i + 1;
			
	i = 0;	
	n = n + 1;


print" \n the largest palindrome is: ", t
		
		





#this program will find the 10001st prime

long long n = 3;
long long i = 3;
long long temp = 3;
long long total = 0;

while(count != 10001):
	
	n = n + 2;

	while i * i < n:

		while n%i == 0:
		        temp = n / i;
			count = count + 1;
		
			if temp > total:
				total = n;
		    
		i = i + 1;


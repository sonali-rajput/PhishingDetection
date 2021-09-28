
import dns.resolver


result = dns.resolver.query('geeksforgeeks.org', 'NS')


for val in result:
	print('NS Record : ', val.to_text())

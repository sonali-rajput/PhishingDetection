# Import libraries
import dns.resolver
def countmxservers(url):
	result = dns.resolver.query(url, 'MX')
	return len(result)


# Finding MX record
result = dns.resolver.query('geeksforgeeks.org', 'MX')

# Printing record
for val in result:
	print('MX Record : ', val.to_text())

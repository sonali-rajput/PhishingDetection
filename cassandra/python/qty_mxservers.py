# Import libraries
import dns.resolver

# Finding MX record
result = dns.resolver.query('geeksforgeeks.org', 'MX')

# Printing record
for val in result:
	print('MX Record : ', val.to_text())

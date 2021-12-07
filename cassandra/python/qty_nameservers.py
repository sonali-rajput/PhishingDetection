
import dns.resolver


# result = dns.resolver.query('geeksforgeeks.org', 'NS')


# for val in result:
# 	print('NS Record : ', val.to_text())

url = "github.com"
def countnameservers(url):
	try:
		result = dns.resolver.resolve(url, 'NS')
		return len(result)
	except:
		return 0

print(countnameservers(url))

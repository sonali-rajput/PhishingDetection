import json
f = open('auth.json')
data = json.load(f)
print(data)
print(data['Username'])
print(data['Password'])

f.close()

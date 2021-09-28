import requests
responses = requests.get("https://forms.gle/hK9oHutvPAsnP3dAA")
count = 0
for response in responses.history:
    print(response.url)
    count+=1
print(count)
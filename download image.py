import requests
import json

with open('1page.json','r') as file:
    data =file.read()
image_links = json.loads(data)
# print(image_links)
hitung = 0
for image in image_links:
    url = image[0]
    r = requests.get(url)
    hitung+=1
    print(hitung)
    with open(f'images/{hitung}.png', 'wb') as file:
        file.write(r.content)
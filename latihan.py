import requests

url = 'https://www.instagram.com/p/B_fsuWajeS3/?__a=1'
res = requests.get(url).json()

date = res['graphql']['shortcode_media']['accessibility_caption'].split('on')[1].split('.')[0]
print(username)


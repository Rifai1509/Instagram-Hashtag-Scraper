import requests

url = 'https://www.instagram.com/p/B_fsuWajeS3/?__a=1'

res = requests.get(url).json()

image = res['graphql']['shortcode_media']['display_url']
username = res['graphql']['shortcode_media']['owner']['username']
date = res['graphql']['shortcode_media']['accessibility_caption'].split('on')[1].split('.')[0]

print(f'image ink   = {image}')
print(f'Username    = {username}')
print(f'Date upload = {date}')



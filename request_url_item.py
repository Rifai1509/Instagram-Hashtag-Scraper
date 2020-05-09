import requests
import csv
import json
url = 'https://www.instagram.com/explore/tags/golfing/?__a=1'
r = requests.get(url).json()
print(r)
# count =0
# area = r['graphql']['hashtag']['edge_hashtag_to_media']['edges']
#
# hitung_halaman = 0
# links = []
# for a in area:
#     hitung_halaman += 1
#     shortcode = a['node']['shortcode']
#     link = 'https://www.instagram.com/p/'+shortcode+'?__a=1'
#     links.append(link)
#
# hitung=0
# datas = []
# image_link =[]
# for url in links:
#     res = requests.get(url).json()
#
#     image = res['graphql']['shortcode_media']['display_url']
#     username = res['graphql']['shortcode_media']['owner']['username']
#     try:
#         date = res['graphql']['shortcode_media']['accessibility_caption'].split('on')[1].split('.')[0]
#     except:
#         date = ''
#     print(f'image ink   = {image}')
#     print(f'Username    = {username}')
#     print(f'Date upload = {date}')
#     datas.append([image,username,date])
#     hitung+=1
#     print(hitung)
#     image_link.append([image])
#
# with open('url.json', 'w') as file:
#     json.dump(image_link, file)
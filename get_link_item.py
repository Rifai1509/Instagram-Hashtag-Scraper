import requests
url = 'https://www.instagram.com/explore/tags/golfing/?__a=1'
r = requests.get(url).json()
count =0
area = r['graphql']['hashtag']['edge_hashtag_to_media']['edges']

hitung = 0
for a in area:
    print(a['node']['shortcode'])
    hitung +=1
    print(hitung)